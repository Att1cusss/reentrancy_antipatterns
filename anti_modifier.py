from slither.core.cfg.node import NodeType


def anti_modifier(function):
    modifier = function.modifiers
    if len(modifier) == 0:
        return False
    for modifier in modifier:
        nodes = modifier.nodes
        for node in nodes:
            if node.type == NodeType.EXPRESSION:
                irslist = node.irs
                if (len(irslist[0].used) == 3
                        and str(irslist[0].used[0].type) == "address"
                        and str(irslist[0].used[1].type) == "address"
                        and str(irslist[0].used[2].type) == "bool"):
                    if str(irslist[1].expression)[:7] == "require":
                        return True
                    else:
                        pass
                else:
                    pass

    return False