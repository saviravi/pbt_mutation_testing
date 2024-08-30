import coverage

def pytest_addoption(parser):
    group = parser.getgroup('pbt_finder')
    group.addoption(
        '--hyp_only',
        action='append',
        dest='dest_hyp',
        default=[],
        help='Collects only the hypothesis tests.'
    )


def pytest_collection_modifyitems(config, items):
    print("pytest_collection_modifyitems hook is called")
    selected = []
    deselected = []
    # print(items)
    for item in items:
        # if item.originalname == "test_stability":
            # print("!!!")
            # print(dir(item.keywords.node), "\n\n", dir(item.keywords.parent), "\n\n", item.keywords._markers)
            # print()
            # print(item.keywords.node.path, item.keywords.node.location)
            # print("!!!")
        if hasattr(item._obj, "is_hypothesis_test") and item._obj.is_hypothesis_test:
            selected.append(item)
            # coverage.Coverage.switch_context()
        else:
            deselected.append(item)
            # print(item.__dict__)
            # print(dict(item.keywords))
            # print()
    # print(selected)
    config.hook.pytest_deselected(items=deselected)
    items[:] = selected
