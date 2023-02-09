import lib_complejos_extend as lb
import math
import unittest

class Test(unittest.TestCase):
    
    def test_suma_Vector(self):
        a = [(4,6),(-6,-1),(3,-8)]
        b = [(5,-6),(3,0),(7,4)]
        self.assertEqual(lb.sum_vector(a,b), [(9, 0), (-3, -1), (10, -4)])
        
    def test_resta_Vector(self):
        a = [(7,3),(-1,-4),(3,-4)]
        b = [(5,-2),(8,5),(7,8)]
        self.assertEqual(lb.resta_vector(a,b), [(2, 5), (-9, -9), (-4, -12)])

    def test_inversoAditivo_Vector(self):
        a = [(-6,3),(2,1),(7,6)]

        self.assertEqual(lb.inverso_aditivo_vector(a),[(6, -3), (-2, -1), (-7, -6)])
        
    def test_prodcutoEscalar_Vector(self):
        a = [(3,-5),(7,8),(7,9)]
        b = (-1,1)

        self.assertEqual(lb.esc_vector(a,b),[(2, 8), (-15, -1), (-16, -2)] )

    def test_suma_Matriz(self):
        a = [[(-4,-5),(-2,-1),(5,-6)],[(-4,3),(6,-8),(2,-1)], [(3,4),(5,6),(-8,-2)]]

        b = [[(-9,-7),(-5,-3),(4,-1)],[(-2,3),(4,-5),(6,-7)], [(8,9),(8,5),(-7,-9)]]

        self.assertEqual(lb.suma_Matriz(a,b),[[(-13, -12), (-7, -4), (9, -7)],[(-6, 6), (10, -13), (8, -8)],[(11, 13), (13, 11), (-15, -11)]])

    def test_inversoAditivo_Matriz(self):
        a = [[(5,6),(-11,3)],[(-4,-5),(-6,-6)]]

        self.assertEqual(lb.inversoAditivo_Matriz(a),[[(-5, -6), (11, -3)], [(4, 5), (6, 6)]])


    def test_productoEscalar_Matriz(self):
        a = [[(5,-22),[4,-5]],[(1,-6),(-7,-3)]]
        b = [-3,7]

        self.assertEqual(lb.productoEscalar_Matriz(a,b),[[(139, 101), (23, 43)], [(39, 25), (42, -40)]])
        
    def test_transpuesta_Matriz_Vector(self):
        a = [[(3,1),(-4,-5),(3,-5)],[(5,1),(-6,-7),(4,-2)]]

        self.assertEqual(lb.transpuesta_Matriz_Vector(a),[[(3, 1), (5, 1)], [(-4, -5), (-6, -7)], [(3, -5), (4, -2)]])
        
    def test_Conjugado_Matriz_Vector(self):
        a = [[(-4,2),(7,2)],[(4,-5),(3,7)]]

        self.assertEqual(lb.conjugado_Matriz_Vector(a),[[(-4, -2), (7, -2)], [(4, 5), (3, -7)]])
        
    def test_adjunta_Matriz_Vector(self):
        a = [[(7,7),(3,8),(8,4)],[(5,0),(8,-6),(-10,-1)]]

        self.assertEqual(lb.adjunta_Matriz_Vector(a),[[(7, -7), (5, 0)], [(3, -8), (8, 6)], [(8, -4), (-10, 1)]])

    def test_Producto_Matriz(self):
        a = [[(-4,8),(9,6)],[(7,4),(2,3)]]
        b = [[(6,7),(8,0)],[(3,2),(4,5)]]
        self.assertEqual(lb.producto_Matriz(a,b),[[(-65, 56), (-26, 133)], [(14, 86), (49, 54)]],[[[-33, 153], [120, 0], [-44, -22]], [[87, 0], [-26, -117], [107, 70]],[[0, 165], [147, 26], [69, -36]]])

    def test_accion_MatrizSobreVector(self):
        a = [[(-1,2),(3,-4),(-5,6)],[(-7,-8),(9,-1),(2,-3)],[(-4,5),(6,-7),(8,-9)]]

        b = [[(1,-2)],[(3,4)],[(-5,6)]]

        self.assertEqual(lb.accion_MatrizSobreVector(a,b),[[(17, -56)], [(16, 66)], [(66, 109)]])
    def test_productoInterno_Vector(self):
        a = [[[1,-2]],[[-3,-4]],[[-5,-6]]]

        b = [[[1,-2]],[[3,-4]],[[-5,-6]]]

        self.assertEqual(lb.productoInterno_Vector(a,b),[[(73, 24)]])

    def test_normaVector(self):
        a = [[(6,3)],[(4,2)],[(7,-8)]]

        self.assertEqual(lb.normaVector(a),13.341664064126334)
        
    def test_distanciaVector(self):
        a = [(1,2),(-3,-4),(5,-6)]
        b = [(9,-8),(7,6),(5,4)]

        self.assertEqual(lb.distanciaVector(a,b),21.540659228538015)
        
    def test_matrizUnitaria(self):
        a = [[(1/math.sqrt(2),0),(0,1/math.sqrt(2))],[(0,1/math.sqrt(2)),(1/math.sqrt(2),0)]]

        b = [[(0,1),(1,0),(0,0)],[(0,0),(0,1),(1,0)],[(1,0),(0,0),(0,1)]]

        self.assertEqual(lb.matrizUnitaria(a),True)
        self.assertEqual(lb.matrizUnitaria(b),False)

    def test_productoTensorial_Matriz_Vector(self):
        v1 = [[(1,1)]]
        v2 = [[(-1,2),(-2,-2)],[(2,3),(3,1)]]
        self.assertEqual(lb.productoTensorial_Matriz_Vector(v1,v2),[[(-3, 1), (0, -4)], [(-1, 5), (2, 4)]])


    



  
if __name__=="__main__":
    unittest.main()
