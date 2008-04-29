import unittest
from Simul_farfield import check_input
from Simul_farfield import reflections


class test_gen_miller(unittest.TestCase):
    def test_(self):  ## test method names begin 'test*'
        param = {}
        param['theta_min'] = 0 
        param['theta_max'] = 5
        param['wavelength'] = 0.2647
        param['unit_cell'] = [8.5312,4.8321,10.125,90.00,92.031,90.00]
        param['sgno'] = 4
        hkl = reflections.gen_miller(param)
        self.assertEquals(len(hkl),498)

    def test_open_structure(self):
        param = {}
        param['structure_file'] = 'oPPA.cif'
#        param['structure_datablock'] = 'oPPA'
        structure = reflections.open_structure(param)
        self.assertEquals(param['sgno'],4)
        self.assertEquals([8.5312,4.8321,10.125,90.00,92.031,90.00],
                          param['unit_cell'])
        

    def test_calc_intensity(self):
        myinput = check_input.parse_input(input_file='simul.inp')
        myinput.read()
        myinput.check()
        myinput.initialize()
        myinput.param['structure_file'] = 'oPPA.cif'
        myinput.param['structure_datablock'] = 'oPPA'

        xtal_structure = reflections.open_structure(myinput.param)
        hkl = reflections.gen_miller(myinput.param)
        hkl = reflections.calc_intensity(hkl,xtal_structure)



if __name__ == '__main__':
    unittest.main()
