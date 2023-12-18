class Tree:
    """ """

    def __init__(self, child_count=0, meta_count=0):
        self.child_count = child_count
        self.meta_count = meta_count
        self.children = []
        self.metadata = []

    def add_child(self, child):
        """

        @param child:
        """
        self.children.append(child)

    def get_child(self):
        """

        @return:
        """
        return self.children

    def add_meta(self, meta):
        """

        @param meta:
        """
        self.metadata += meta

    def get_meta(self):
        """

        @return:
        """
        return self.metadata


def build_tree(tree_data):
    """

    @param tree_data:
    @return:
    """
    child_count = tree_data[0]
    meta_count = tree_data[1]
    root = Tree(child_count, meta_count)
    for _ in range(child_count):
        child, data_without_root = build_tree(tree_data[2:])
        root.add_child(child)
        tree_data = tree_data[:2] + data_without_root
    root.add_meta(tree_data[2 : meta_count + 2])
    tree_data = tree_data[(meta_count + 2) :]

    return root, tree_data


def sum_tree_metadata(root):
    """

    @param root:
    @return:
    """
    metadata_sum = sum(root.metadata)
    for child in root.children:
        metadata_sum += sum_tree_metadata(child)
    return metadata_sum


def sum_root_value(root):
    """

    @param root:
    @return:
    """
    metadata_sum = 0
    if root.child_count == 0:
        return sum(root.metadata)

    for child_index in root.metadata:
        if child_index <= root.child_count:
            metadata_sum += sum_root_value(root.children[child_index - 1])
    return metadata_sum
