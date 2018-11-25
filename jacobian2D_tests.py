import unittest
from grid import *
from jacobian2D import *


class TestJakobian2D(unittest.TestCase):

    def test_ShapeFunctionN1(self):
        self.assertAlmostEqual(0.622008, shape_function_n1(tab_eta[0], tab_ksi[0]), None, None, 0.00001)

    def test_ShapeFunctionN2(self):
        self.assertAlmostEqual(0.166666, shape_function_n2(tab_eta[0], tab_ksi[0]), None, None, 0.00001)

    def test_ShapeFunctionN3(self):
        self.assertAlmostEqual(0.044658, shape_function_n3(tab_eta[0], tab_ksi[0]), None, None, 0.00001)

    def test_ShapeFunctionN4(self):
        self.assertAlmostEqual(0.166666, shape_function_n4(tab_eta[0], tab_ksi[0]), None, None, 0.00001)

    def test_xp_for_node1(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.005283, xp_for_node(element_to_test[0], 1), None, None, 0.00001)

    def test_xp_for_node2(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.019717, xp_for_node(element_to_test[0], 2), None, None, 0.00001)

    def test_xp_for_node3(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.019717, xp_for_node(element_to_test[0], 3), None, None, 0.00001)

    def test_xp_for_node4(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.005283, xp_for_node(element_to_test[0], 4), None, None, 0.00001)

    def test_yp_for_node1(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.005283, yp_for_node(element_to_test[0], 1), None, None, 0.00001)

    def test_yp_for_node2(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.005283, yp_for_node(element_to_test[0], 2), None, None, 0.00001)

    def test_yp_for_node3(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.019717, yp_for_node(element_to_test[0], 3), None, None, 0.00001)

    def test_yp_for_node4(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.019717, yp_for_node(element_to_test[0], 4), None, None, 0.00001)

    def test_dn_d_eta_1_1(self):
        self.assertAlmostEqual(-0.394337, dn_d_eta(1, 1), None, None, 0.00001)

    def test_dn_d_eta_1_4(self):
        self.assertAlmostEqual(-0.105662, dn_d_eta(1, 4), None, None, 0.00001)

    def test_dn_d_eta_2_1(self):
        self.assertAlmostEqual(0.394337, dn_d_eta(2, 1), None, None, 0.00001)

    def test_dn_d_eta_3_1(self):
        self.assertAlmostEqual(0.105662, dn_d_eta(3, 1), None, None, 0.00001)

    def test_dn_d_eta_4_1(self):
        self.assertAlmostEqual(-0.105662, dn_d_eta(4, 1), None, None, 0.00001)

    def test_dn_d_eta_4_3(self):
        self.assertAlmostEqual(-0.394337, dn_d_eta(4, 3), None, None, 0.00001)

    def test_dn_d_ksi_1_1(self):
        self.assertAlmostEqual(-0.394337, dn_d_ksi(1, 1), None, None, 0.00001)

    def test_dn_d_ksi_2_1(self):
        self.assertAlmostEqual(-0.105662, dn_d_ksi(2, 1), None, None, 0.00001)

    def test_dn_d_ksi_3_1(self):
        self.assertAlmostEqual(0.105662, dn_d_ksi(3, 1), None, None, 0.00001)

    def test_dn_d_ksi_4_1(self):
        self.assertAlmostEqual(0.394337, dn_d_ksi(4, 1), None, None, 0.00001)

    def test_jakobian_1_1(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.0125, j_1_1(element_to_test[0], 1), None, None, 0.00001)

    def test_jakobian_1_2(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0, j_1_2(element_to_test[0], 1), None, None, 0.00001)

    def test_jakobian_2_1(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0, j_2_1(element_to_test[0], 1), None, None, 0.00001)

    def test_jakobian_2_2(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.0125, j_2_2(element_to_test[0], 1), None, None, 0.00001)

    def test_det_j_1(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.00015625, det_jacobian(element_to_test[0], 1), None, None, 0.00000001)

    def test_det_j_2(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.00015625, det_jacobian(element_to_test[0], 2), None, None, 0.00000001)

    def test_det_j_3(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.00015625, det_jacobian(element_to_test[0], 3), None, None, 0.00000001)

    def test_det_j_4(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertAlmostEqual(0.00015625, det_jacobian(element_to_test[0], 4), None, None, 0.00000001)

    def test_jacobian_2D_11(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertEqual(80, jacobian_2d_11(element_to_test[0], 1))

    def test_jacobian_2D_12(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertEqual(0, jacobian_2d_12(element_to_test[0], 1))

    def test_jacobian_2D_21(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertEqual(0, jacobian_2d_21(element_to_test[0], 1))

    def test_jacobian_2D_22(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertEqual(80, jacobian_2d_22(element_to_test[0], 1))

    def test_create_jacobian_2d_el_0_0(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertEqual(80, create_jacobian_2d(element_to_test[0])[0][0])

    def test_create_jacobian_2d_el_0_1(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertEqual(0, create_jacobian_2d(element_to_test[0])[0][1])

    def test_create_jacobian_2d_el_3_3(self):
        node_to_test = create_nodes(1, 1, 0.025, 0.025, 20)
        element_to_test = create_elements(1, 1, node_to_test)
        self.assertEqual(80, create_jacobian_2d(element_to_test[0])[3][3])

    def test_jacobian_2D_main(self):
        self.assertEqual(80, jacobian_2d_main()[0][0])


if __name__ == '__main__':
    unittest.main()
