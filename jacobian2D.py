from const import *
from grid import *


def shape_function_n1(eta, ksi):
    return 0.25 * (1 - ksi) * (1 - eta)


def shape_function_n2(eta, ksi):
    return 0.25 * (1 + ksi) * (1 - eta)


def shape_function_n3(eta, ksi):
    return 0.25 * (1 + ksi) * (1 + eta)


def shape_function_n4(eta, ksi):
    return 0.25 * (1 - ksi) * (1 + eta)


def xp_for_node(element, node_id):
    xp = 0.0
    node_id -= 1
    xp += float(shape_function_n1(tab_eta[node_id], tab_ksi[node_id])) * float(element.node1.x)
    xp += float(shape_function_n2(tab_eta[node_id], tab_ksi[node_id])) * float(element.node2.x)
    xp += float(shape_function_n3(tab_eta[node_id], tab_ksi[node_id])) * float(element.node3.x)
    xp += float(shape_function_n4(tab_eta[node_id], tab_ksi[node_id])) * float(element.node4.x)
    return xp


def yp_for_node(element, node_id):
    y = 0.0
    node_id -= 1
    y += float(shape_function_n1(tab_eta[node_id], tab_ksi[node_id])) * float(element.node1.y)
    y += float(shape_function_n2(tab_eta[node_id], tab_ksi[node_id])) * float(element.node2.y)
    y += float(shape_function_n3(tab_eta[node_id], tab_ksi[node_id])) * float(element.node3.y)
    y += float(shape_function_n4(tab_eta[node_id], tab_ksi[node_id])) * float(element.node4.y)
    return y


def dn_d_eta(shape_function_number, integration_point):
    # Pochodne funkcji ksztaltu wzgledem osi eta
    if shape_function_number == 1:
        return -0.25*(1 - tab_eta[integration_point - 1])
    elif shape_function_number == 2:
        return 0.25*(1 - tab_eta[integration_point - 1])
    elif shape_function_number == 3:
        return 0.25*(1 + tab_eta[integration_point - 1])
    elif shape_function_number == 4:
        return -0.25*(1 + tab_eta[integration_point - 1])


def dn_d_ksi(shape_function_number, integration_point):
    # Pochodne funkcji ksztaltu wzgledem osi ksi
    if shape_function_number == 1:
        return -0.25*(1 - tab_ksi[integration_point - 1])
    elif shape_function_number == 2:
        return -0.25*(1 + tab_ksi[integration_point - 1])
    elif shape_function_number == 3:
        return 0.25*(1 + tab_ksi[integration_point - 1])
    elif shape_function_number == 4:
        return 0.25*(1 - tab_ksi[integration_point - 1])


def j_1_1(element, integration_point):
    j_value = 0.0
    j_value += dn_d_eta(1, integration_point) * element.node1.x
    j_value += dn_d_eta(2, integration_point) * element.node2.x
    j_value += dn_d_eta(3, integration_point) * element.node3.x
    j_value += dn_d_eta(4, integration_point) * element.node4.x
    return j_value


def j_1_2(element, integration_point):
    j_value = 0.0
    j_value += dn_d_eta(1, integration_point) * element.node1.y
    j_value += dn_d_eta(2, integration_point) * element.node2.y
    j_value += dn_d_eta(3, integration_point) * element.node3.y
    j_value += dn_d_eta(4, integration_point) * element.node4.y
    return j_value


def j_2_1(element, integration_point):
    j_value = 0.0
    j_value += dn_d_ksi(1, integration_point) * element.node1.x
    j_value += dn_d_ksi(2, integration_point) * element.node2.x
    j_value += dn_d_ksi(3, integration_point) * element.node3.x
    j_value += dn_d_ksi(4, integration_point) * element.node4.x
    return j_value


def j_2_2(element, integration_point):
    j_value = 0.0
    j_value += dn_d_ksi(1, integration_point) * element.node1.y
    j_value += dn_d_ksi(2, integration_point) * element.node2.y
    j_value += dn_d_ksi(3, integration_point) * element.node3.y
    j_value += dn_d_ksi(4, integration_point) * element.node4.y
    return j_value


def det_jacobian(element, integration_point):
    det_value = 0.0
    det_value += j_1_1(element, integration_point) * j_2_2(element, integration_point)
    det_value -= j_1_2(element, integration_point) * j_2_1(element, integration_point)
    return det_value


def jacobian_2d_11(element, integration_point):
    return j_2_2(element, integration_point) / det_jacobian(element, integration_point)


def jacobian_2d_12(element, integration_point):
    return j_1_2(element, integration_point) / det_jacobian(element, integration_point)


def jacobian_2d_21(element, integration_point):
    return j_2_1(element, integration_point) / det_jacobian(element, integration_point)


def jacobian_2d_22(element, integration_point):
    return j_2_2(element, integration_point) / det_jacobian(element, integration_point)


def create_jacobian_2d(element):
    jacobian = []
    for i in range(0, 4, 1):
        jacobian.append([])
        jacobian[i].append(jacobian_2d_11(element, i+1))
        jacobian[i].append(jacobian_2d_12(element, i+1))
        jacobian[i].append(jacobian_2d_21(element, i+1))
        jacobian[i].append(jacobian_2d_22(element, i+1))
    return jacobian


def jacobian_2d_main():
    mes_input = read_file()

    nH = mes_input[0]
    nL = mes_input[1]
    node_height = mes_input[2]
    node_length = mes_input[3]

    node = create_nodes(nH, nL, node_height, node_length, 20)
    element = create_elements(1, 1, node)
    jacobian_2D = create_jacobian_2d(element[0])
    return jacobian_2D


def main():

    jacobian_2d = jacobian_2d_main()

    for i in range(len(jacobian_2d)):
        print(jacobian_2d[i])


if __name__ == "__main__":
    main()
