init python in style_dumper:
    import types

    sort_by_depth = False
    dump_none = True
    dump_zero_false = True
    dump_only_modified = True
    dump_computed = False

    ignored_attrs = [
        "add_properties",
        "clear",
        "copy",
        "delattr",
        "get_offset",
        "get_placement",
        "inspect",
        "set_parent",
        "set_prefix",
        "setattr",
        "setdefault",
        "take",

        "name",
        "parent",

        "properties",

        # Not sure what these attributes are
        "debug",
        "help",
        "prefix",
    ]

    def write_style_statement(file, style, prop_count = 0):
        name = style.name[0]

        if has_parent(style):
            file.write("style %s is %s" % (name, getattr(style, "parent")[0]))
        else:
            file.write("style %s" % name)

        file.write(":\n" if prop_count > 0 else "\n")

    def format_value(value):
        if isinstance(value, renpy.color.Color):
            return format_value(value.hexcode)

        elif isinstance(value, renpy.display.im.Image):
            return format_value(value.filename)

        elif isinstance(value, renpy.display.image.DynamicImage):
            return format_value(value.name)

        elif isinstance(value, renpy.display.image.ImageReference):
            return format_value(value.name)

        elif isinstance(value, renpy.display.imagelike.Frame):
            return "Frame(%s, Borders(%s, %s, %s, %s))" % (
                format_value(value.image),
                format_value(value.left),
                format_value(value.top),
                format_value(value.right),
                format_value(value.bottom)
            )

        elif isinstance(value, renpy.display.imagelike.Solid):
            return "Solid(%s)" % format_value(value.color)

        elif isinstance(value, renpy.display.layout.Null):
            return "Null()"

        elif isinstance(value, renpy.styledata.styleclass.Style):
            return format_value(value.name[0])

        elif isinstance(value, renpy.text.font.FontGroup):
            return ", ".join([format_value(x) for x in value.fonts])

        elif isinstance(value, (int, float, bool, types.NoneType)):
            return str(value)

        elif isinstance(value, dict):
            return "{%s}" % (", ".join(["%s: %s" % (format_value(key), format_value(value[key])) for key in sorted(value.keys())]))

        elif isinstance(value, list):
            return "[%s]" % (", ".join([format_value(x) for x in value]))

        elif isinstance(value, tuple):
            return "(%s)" % (", ".join([format_value(x) for x in value]))

        elif isinstance(value, (str, unicode)):
            return "\"%s\"" % value

        else:
            return str(type(value))

    def has_parent(style):
        return hasattr(style, "parent") and getattr(style, "parent")

    def is_attr_unchanged(style, key):
        if not has_parent(style):
            return False

        parent = renpy.style.styles[style.parent]

        return getattr(style, key) == getattr(parent, key)

    def is_attr_valid(style, key):
        if key.startswith("_") or key in ignored_attrs:
            return False

        if dump_only_modified and is_attr_unchanged(style, key):
            return False

        value = getattr(style, key)

        if not dump_none and value == None:
            return False

        if not dump_zero_false and (value == 0 or value == 0.0 or value == False):
            return False

        return True

    def write_style(file, style):
        if not style:
            return

        props = {}

        if dump_computed:
            for key in dir(style):
                if is_attr_valid(style, key):
                    props[key] = getattr(style, key)

        else:
            for prop_dict in style.properties:
                props.update(prop_dict)

        write_style_statement(file, style, len(props))

        for key in sorted(props.keys()):
            value = props[key]
            file.write("    %-20s %s\n" % (key, format_value(value)))

    def get_depth(style):
        result = 1

        if style.parent:
            parent = renpy.style.styles[style.parent]
            result += get_depth(parent)

        return result

    def dump(path = "styles.txt"):
        with open(path, "w") as out_file:
            styles = renpy.style.styles

            keys = styles.keys()
            keys = sorted(keys)

            if sort_by_depth:
                keys = sorted(keys, key = lambda x: styles[x].parent)
                keys = sorted(keys, key = lambda x: get_depth(styles[x]))

            for key in keys:
                style = styles[key]
                write_style(out_file, style)

                out_file.write("\n")



init python in style_hierarchy_dumper:
    class StyleNode:
        def __init__(self, style):
            self.style = style
            self.children = []

    def build_graph():
        nodes = {key: StyleNode(style) for key, style in renpy.style.styles.items()}
        roots = []

        for node in sorted(nodes.values(), key = lambda x: x.style.name):
            if not node.style.parent:
                roots.append(node)

            else:
                parent = nodes[node.style.parent]
                parent.children.append(node)

        return roots

    def write_node(file, node, level = 0):
        file.write("%s%s\n" % ("    " * level, node.style.name[0]))

        for i, child in enumerate(node.children):
            write_node(file, child, level + 1)

    def dump(path = "style_hierarchy.txt"):
        roots = build_graph()

        with open(path, "w") as out_file:
            for root in roots:
                write_node(file, root)
