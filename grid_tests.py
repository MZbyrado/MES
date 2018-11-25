import unittest
from grid import *


class TestMes1(unittest.TestCase):

    def test_init_node(self):
        self.assertIsNotNone(Node(1, 1, 1, 1))

    def test_init_element(self):
        self.assertIsNotNone(Element(1, 2, 3, 4, 5))

    def test_create_4_nodes(self):
        self.assertEqual(4, len(create_nodes(1, 1, 1, 1, 20)))

    def test_create_nodes_for_2_elements_2x1(self):
        self.assertEqual(6, len(create_nodes(2, 1, 1, 1, 20)))

    def test_create_nodes_for_nH3_nL3(self):
        self.assertEqual(16, len(create_nodes(3, 3, 1, 1, 20)))

    def test_create_nodes_for_nH7_nL3(self):
        self.assertEqual(32, len(create_nodes(7, 3, 1, 1, 20)))

    def test_node_id(self):
        node_to_test = create_nodes(3, 3, 1, 1, 20)
        self.assertEqual(6, node_to_test[5].node_id)

    def test_node_coordinates_height_1_length_1(self):
        node_to_test = create_nodes(3, 3, 1, 1, 20)
        self.assertEqual(0, node_to_test[3].x)
        self.assertEqual(3, node_to_test[3].y)

        self.assertEqual(1, node_to_test[7].x)
        self.assertEqual(3, node_to_test[7].y)

        self.assertEqual(2, node_to_test[10].x)
        self.assertEqual(2, node_to_test[10].y)

    def test_node_coordinates_height_025_length_025(self):
        node_to_test = create_nodes(3, 3, 0.25, 0.25, 20)
        self.assertEqual(0.75, node_to_test[3].y)
        self.assertEqual(0.75, node_to_test[12].x)

        self.assertEqual(0.5, node_to_test[10].x)
        self.assertEqual(0.5, node_to_test[10].y)

    def test_element_node1_coordinates_1x1(self):
        node_to_test = create_nodes(1, 1, 0.25, 0.25, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertEqual(0, element_to_test[0].node1.x)
        self.assertEqual(0, element_to_test[0].node1.y)

    def test_element_node2_coordinates_1x1(self):
        node_to_test = create_nodes(1, 1, 0.25, 0.25, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertEqual(0.25, element_to_test[0].node2.x)
        self.assertEqual(0, element_to_test[0].node2.y)

    def test_element_node3_coordinates_1x1(self):
        node_to_test = create_nodes(1, 1, 0.25, 0.25, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertEqual(0.25, element_to_test[0].node3.x)
        self.assertEqual(0.25, element_to_test[0].node3.y)

    def test_element_node3_coordinates_1x1(self):
        node_to_test = create_nodes(1, 1, 0.25, 0.25, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertEqual(0, element_to_test[0].node4.x)
        self.assertEqual(0.25, element_to_test[0].node4.y)

    def test_element_node_coordinates_2x2(self):
        node_to_test = create_nodes(2, 2, 0.25, 0.25, 20)
        element_to_test = create_elements(2, 2, node_to_test)
        self.assertEqual(0.25, element_to_test[1].node2.x)
        self.assertEqual(0.25, element_to_test[1].node2.y)

        self.assertEqual(0.25, element_to_test[1].node3.x)
        self.assertEqual(0.5, element_to_test[1].node3.y)

        self.assertEqual(0.5, element_to_test[3].node3.x)
        self.assertEqual(0.5, element_to_test[3].node3.y)

    def test_create_one_element(self):
        node_to_test = create_nodes(1, 1, 0.25, 0.25, 20)
        self.assertIsNotNone(create_elements(1, 1, node_to_test))

    def test_element_nodes_id_1x1(self):
        node_to_test = create_nodes(1, 1, 0.25, 0.25, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertEqual(1, element_to_test[0].node1.node_id)
        self.assertEqual(3, element_to_test[0].node2.node_id)
        self.assertEqual(4, element_to_test[0].node3.node_id)
        self.assertEqual(2, element_to_test[0].node4.node_id)

    def test_element_nodes_id_2x1_el0(self):
        node_to_test = create_nodes(2, 1, 0.25, 0.25, 20)
        element_to_test = create_elements(2, 1, node_to_test)
        self.assertEqual(1, element_to_test[0].node1.node_id)
        self.assertEqual(4, element_to_test[0].node2.node_id)
        self.assertEqual(5, element_to_test[0].node3.node_id)
        self.assertEqual(2, element_to_test[0].node4.node_id)

    def test_element_nodes_id_2x1_el1(self):
        node_to_test = create_nodes(2, 1, 0.25, 0.25, 20)
        element_to_test = create_elements(2, 1, node_to_test)
        self.assertEqual(2, element_to_test[1].node1.node_id)
        self.assertEqual(5, element_to_test[1].node2.node_id)
        self.assertEqual(6, element_to_test[1].node3.node_id)
        self.assertEqual(3, element_to_test[1].node4.node_id)

    def test_element_nodes_id_1x2_el0(self):
        node_to_test = create_nodes(1, 2, 0.25, 0.25, 20)
        element_to_test = create_elements(1, 2, node_to_test)
        self.assertEqual(1, element_to_test[0].node1.node_id)
        self.assertEqual(3, element_to_test[0].node2.node_id)
        self.assertEqual(4, element_to_test[0].node3.node_id)
        self.assertEqual(2, element_to_test[0].node4.node_id)

    def test_element_nodes_id_1x2_el1(self):
        node_to_test = create_nodes(1, 2, 0.25, 0.25, 20)
        element_to_test = create_elements(1, 2, node_to_test)
        self.assertEqual(3, element_to_test[1].node1.node_id)
        self.assertEqual(5, element_to_test[1].node2.node_id)
        self.assertEqual(6, element_to_test[1].node3.node_id)
        self.assertEqual(4, element_to_test[1].node4.node_id)

    def test_element_nodes_id_7x3_el11(self):
        node_to_test = create_nodes(7, 3, 0.25, 0.25, 20)
        element_to_test = create_elements(7, 3, node_to_test)
        self.assertEqual(13, element_to_test[11].node1.node_id)
        self.assertEqual(21, element_to_test[11].node2.node_id)
        self.assertEqual(22, element_to_test[11].node3.node_id)
        self.assertEqual(14, element_to_test[11].node4.node_id)

    def test_element_nodes_id_7x3_el20(self):
        node_to_test = create_nodes(7, 3, 0.25, 0.25, 20)
        element_to_test = create_elements(7, 3, node_to_test)
        self.assertEqual(23, element_to_test[20].node1.node_id)
        self.assertEqual(31, element_to_test[20].node2.node_id)
        self.assertEqual(32, element_to_test[20].node3.node_id)
        self.assertEqual(24, element_to_test[20].node4.node_id)


if __name__ == '__main__':
    unittest.main()
