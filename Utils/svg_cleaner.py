################################################################################
#
# Copyright (c) 2020–2021 Dominus Iniquitatis <zerosaiko@gmail.com>
#
# See LICENSE file for the licensing information
#
################################################################################
import re
from argparse import ArgumentParser
from pathlib import Path
from xml.etree import ElementTree

xml_namespaces = {
    "":         "http://www.w3.org/2000/svg",
    "inkscape": "http://www.inkscape.org/namespaces/inkscape",
    "sodipodi": "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd",
    "xlink":    "http://www.w3.org/1999/xlink",
}

idless_tags = [
    "feBlend",
    "feColorMatrix",
    "feComposite",
    "feDisplacementMap",
    "feDistantLight",
    "feFlood",
    "feGaussianBlur",
    "feOffset",
    "feSpecularLighting",
    "feTurbulence",
    "stop",
]

attr_order = [
    "version",
    "id",
    "in",
    "in2",
    "result",
    "x",
    "y",
    "x1",
    "y1",
    "x2",
    "y2",
    "cx",
    "cy",
    "dx",
    "dy",
    "width",
    "height",
    "viewBox",
    "r",
    "rx",
    "ry",
    "rotation",
    "transform",
    "preserveAspectRatio",
    "d",
    "points",
    "xlink:href",
    "mode",
    "type",
    "azimuth",
    "baseFrequency",
    "elevation",
    "k1",
    "k2",
    "k3",
    "k4",
    "numOctaves",
    "offset",
    "operator",
    "scale",
    "seed",
    "specularConstant",
    "specularExponent",
    "spreadMethod",
    "stdDeviation",
    "surfaceScale",
    "values",
    "xChannelSelector",
    "yChannelSelector",
    "filterUnits",
    "gradientUnits",
    "patternUnits",
]
attr_order = [x.replace(ns_name + ":", ns_url) for x in attr_order for ns_name, ns_url in xml_namespaces.items()]

style_order = []

presentation_attrs = [
    "color-interpolation-filters",
    "fill",
    "fill-opacity",
    "filter",
    "flood-color",
    "flood-opacity",
    "font-family",
    "font-size",
    "font-style",
    "font-weight",
    "letter-spacing",
    "line-height", # Non-standard
    "stop-color",
    "stop-opacity",
    "stroke",
    "stroke-dasharray",
    "stroke-linecap",
    "stroke-linejoin",
    "stroke-opacity",
    "stroke-width",
]

def make_comparator(key_order):
    def comparator(item):
        key = item[0]

        try:
            index = len(key_order) - key_order.index(key)
        except ValueError:
            index = 0

        return " " * index + key

    return comparator

def sort_dict(d, comp):
    return {k: v for k, v in sorted(d.items(), key = comp)}

def parse_style_string(string):
    style_dict = {}

    for statement in string.split(";"):
        if statement.strip() == "":
            continue

        key, value = statement.split(":")
        style_dict[key.strip()] = value.strip()

    return style_dict

def dump_style_dict(d):
    return "; ".join(f"{k}: {v}" for k, v in d.items())

def sort_attrs(node):
    comparator = make_comparator(attr_order + presentation_attrs)
    node.attrib = sort_dict(node.attrib, comparator)

def sort_style_props(node):
    style_text = node.attrib.get("style", None)

    if not style_text:
        return

    style_dict = parse_style_string(style_text)

    comparator = make_comparator(style_order)
    style_dict = sort_dict(style_dict, comparator)

    node.attrib["style"] = dump_style_dict(style_dict)

def extract_style_props(node):
    style_text = node.attrib.get("style", None)

    if not style_text:
        return

    style_dict = parse_style_string(style_text)

    for k, v in style_dict.items():
        if k in presentation_attrs:
            node.attrib[k] = v

    style_dict = {k: v for k, v in style_dict.items() if k not in presentation_attrs}

    if len(style_dict) > 0:
        node.attrib["style"] = dump_style_dict(style_dict)
    else:
        node.attrib.pop("style")

def pack_style_props(node):
    style_text = node.attrib.get("style", None)

    if not style_text:
        style_text = node.attrib["style"] = ""

    style_dict = parse_style_string(style_text)

    for k, v in node.attrib.items():
        if k in presentation_attrs:
            style_dict[k] = v

    node.attrib = {k: v for k, v in node.attrib.items() if k not in presentation_attrs}

    if len(style_dict) > 0:
        node.attrib["style"] = dump_style_dict(style_dict)
    else:
        node.attrib.pop("style")

def remove_ids(node):
    if re.sub(r"\{.+\}", "", node.tag) in idless_tags:
        node.attrib.pop("id", None)

def sanitize_attrs(node):
    def hex_replacer(m):
        r = int(m.group(1), 16)
        g = int(m.group(2), 16)
        b = int(m.group(3), 16)
        return f"rgb({r}, {g}, {b})"

    def rgb_replacer(m):
        return f"rgb({m.group(1)}, {m.group(2)}, {m.group(3)})"

    re_space = re.compile(r"\s+")
    re_hex = re.compile(r"#([0-9a-f]{2})([0-9a-f]{2})([0-9a-f]{2})")
    re_rgb = re.compile(r"rgb\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)")

    a = node.attrib

    for k in a.keys():
        a[k] = a[k].strip()
        a[k] = re.sub(re_space, " ", a[k])
        a[k] = re.sub(re_hex, hex_replacer, a[k])
        a[k] = re.sub(re_rgb, rgb_replacer, a[k])

def process_node(node, pack_style):
    if pack_style:
        pack_style_props(node)
    else:
        extract_style_props(node)

    remove_ids(node)
    sort_attrs(node)
    sort_style_props(node)
    sanitize_attrs(node)

def process_xmls(paths, suffix, pack_styles):
    for ns_name, ns_url in xml_namespaces.items():
        ElementTree.register_namespace(ns_name, ns_url)

    for in_path in paths:
        out_path = in_path.with_stem(in_path.stem + suffix)

        with open(in_path, "r", encoding = "utf-8") as in_file:
            root = ElementTree.fromstring(in_file.read())

        with open(out_path, "w", encoding = "utf-8") as out_file:
            process_node(root, pack_styles)

            for node in root.iter():
                process_node(node, pack_styles)

            out_file.write(ElementTree.tostring(root, encoding = "utf-8").decode())
            out_file.write("\n")

if __name__ == "__main__":
    ap = ArgumentParser()
    ap.add_argument("path",
                    type = str,
                    help = "input file or file mask")
    ap.add_argument("-s", "--suffix",
                    type = str,
                    default = "",
                    help = "set output file suffix")
    ap.add_argument("-p", "--pack-styles",
                    action = "store_true",
                    help = "pack presentation attributes into \"style\" attribute")

    args = ap.parse_args()

    process_xmls(Path(".").glob(args.path), args.suffix, args.pack_styles)
