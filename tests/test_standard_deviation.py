import unittest
import numpy as np

from tests.sample_data import SampleData
from pyti import standard_deviation


class TestStandardDeviation(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_close_data()

        self.std_period_6_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
            6.5577905323871235, 3.523047922845588, 3.64000366300183,
            2.6142411263437193, 2.6233540871691017, 2.5428206123646837,
            2.8984064587286413, 2.8167262321117761, 3.8064874447010402,
            4.1082230546389029, 8.3307254586060449, 10.698429168184775,
            14.471698472075328, 14.149189022696682, 16.029104466563318,
            13.032673938988863, 10.08650583700817, 9.4405432400189078,
            10.488392949669004, 10.589531938035151, 8.7339880161737451,
            5.0316216736422801, 3.8436670858265902, 3.9887023788027181,
            4.0649809347646144, 4.083843369507024, 4.8440000688136395,
            11.967095581914025, 11.182192390880525, 11.491860887892189,
            16.916712151006177, 22.056151447309816, 22.859576257373337,
            16.434078820142823, 14.253613810773276, 13.039983767883554,
            13.022551209344496, 12.50387726533919, 16.058846471649176,
            15.333279710051146, 12.463120663247507, 8.355378307812666,
            9.0049564129983466, 6.6962407364132304, 6.4353546910795751,
            5.2716958055891929, 5.3789689222625849, 9.4365405031010461,
            9.4650967594983619, 10.229352700277104, 9.58579104716976,
            6.4664696705389293, 4.0370422341114756, 5.161696103672357,
            5.3648150014701983, 5.8074081998770941, 5.3992755686912774,
            5.2324474834121784, 1.4768265526684596, 1.3318358257182561,
            3.448881944437431, 4.2672145481566792, 4.2827919242786781,
            5.130538633191148, 5.783125164361131, 5.2763611198123055,
            6.6918926072275768, 8.2688781988046696, 8.8089197218879818,
            7.3125547291399391, 5.0221549159698196, 5.0711711336402896,
            4.9256529178035535, 5.6864083567749528, 6.5936466895540216,
            8.2274234524951151, 8.8677071444652373, 7.4646598493612917,
            8.3602240799315091, 8.0184206674381961, 8.3401744586069686,
            6.6355034976003617, 2.6993406602353964, 2.0581391271405236,
            2.0719885778321165, 2.0978504872051325, 2.2254437759692176,
            3.049114078985355, 4.1007641564306905, 4.3524338019089699,
            3.4153872401237066, 3.4531299811426996, 2.9287608301122723,
            2.648205052483652, 2.6683584217017398, 2.7031296676260124,
            1.2711792425408255, 1.158740695755534, 4.2491112796285666,
            4.7691131250998939, 4.4221567136409838, 3.7499159990591719,
            5.0847300813317311, 13.454516589854368, 17.889961896736011,
            19.98118781921303, 18.782584131760668, 12.993947821966982,
            3.989429783816254, 2.5093963417523479, 2.2056057369046482,
            2.4943830232477606, 8.4362062958812629, 9.8113133677403432,
            11.767257964368774, 10.560069602043356, 9.2450563365869662,
            6.762383209096229, 10.628135772561432, 10.820357973129482,
            11.395558345250143, 8.3253558482505863]

        self.std_period_8_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
            np.nan, np.nan, 7.0210000050867709, 4.1373628591859681,
            3.2119864792457009, 2.7914512354687684, 3.4517159293810558,
            2.9480489916456389, 3.3239821213203209, 3.5875118217824093,
            7.0898191594910145, 9.6610417029280189, 14.687200878413067,
            16.195911080093211, 18.167517274756381, 17.864408150605726,
            15.684568394262103, 11.769444625202757, 10.355555358633076,
            8.9695687903998031, 8.9965326654217108, 9.4195188685136966,
            7.8538143599145407, 4.9657714118035772, 4.4569047555450325,
            3.8001832662573869, 4.1709606207683017, 10.62482193128093,
            10.778041168439238, 10.368574688520509, 14.639153956818289,
            18.713909981233599, 19.898422047991648, 19.861963649146077,
            19.509732690194838, 14.34043079398743, 12.959500651755734,
            12.497358506614786, 14.475216998126715, 15.211531281517024,
            17.001755161495186, 16.432812069149929, 14.674135408943185,
            9.7164201961715975, 7.6440704143800264, 5.8451933855335998,
            5.64821447766586, 8.2422530726910797, 10.625605192848331,
            11.692462086440853, 9.3994635105262265, 8.8257479448324467,
            8.2020719290049708, 6.6277963101298756, 4.6265561088752829,
            5.0357789509525652, 5.1546871874052478, 5.4984069121363168,
            4.875291749511721, 4.4419035494770691, 3.0770089256567457,
            3.888717884562241, 3.9120171997869004, 5.1726366238947525,
            6.0172975365073498, 5.404976542832701, 6.0530629790686739,
            7.3309684363176757, 7.7985836626183254, 7.575020980640458,
            9.0041798825402761, 8.6284213710934914, 5.4515083102883279,
            5.1782069083529505, 5.6630795193831744, 7.1805271145548293,
            8.1723628337044669, 8.0955966867356697, 7.9802591257606208,
            7.8027393312495414, 8.0798487211793066, 7.3342765491901138,
            7.2319093260355505, 5.8455966333642975, 2.3867655938529189,
            2.3230690906643527, 2.6017847583094862, 2.8489970039597292,
            3.6898432022435403, 4.8986382947567213, 4.7263741388087315,
            4.3969662837006034, 4.042064536135654, 3.9273398394187429,
            3.2888054170821017, 2.6214268197736392, 2.3381906924555294,
            2.3338621424582748, 3.6274033904630554, 4.3679741544892181,
            4.5729569989543766, 4.3530613201680106, 5.4448558619253422,
            13.02311290140943, 16.948090442373044, 18.927592811629722,
            20.199922736768791, 19.547403736996472, 17.506905933292263,
            11.913134333283477, 4.0137655992489707, 3.0322316157293447,
            7.5580302611574259, 9.5411865651725272, 11.636474598065714,
            11.543465684100253, 12.016773321962457, 12.317852244956159,
            13.544956625991842, 11.53342773667667, 12.324006697151235,
            11.031367937451309]

        self.std_period_10_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
            np.nan, np.nan, np.nan, np.nan, 6.4860058759009869, 4.1526223307955945,
            3.9927105802672158, 3.3004546824810688, 3.5370766334801407,
            3.3311401118002317, 6.4384024933726254, 8.9119850014834938,
            13.351934067142995, 15.482619969214232, 19.070120928358637,
            20.404015100519359, 18.748148353015203, 16.133700409047169,
            14.06749796121858, 10.572570590395159, 9.1555945859470089,
            8.3281877447083907, 8.5784715033234864, 8.6222052476923263,
            7.3341742699653665, 4.63688305270301, 4.7504993889531688,
            9.7508812137387935, 9.598666805574835, 9.6019130616999515,
            13.188306942136279, 16.671782548166032, 17.789894790770031,
            17.598722302106669, 17.607555480531644, 17.578184743849089,
            18.26081734205783, 14.630932263150182, 14.408303315950986,
            13.91782390398089, 15.258254924247829, 17.018062822255114,
            19.390673273509599, 17.141471640439732, 13.282047574744562,
            8.829194250389504, 6.9174080727136875, 7.5843822717769385,
            9.459425928082986, 10.848561399763753, 11.075405435267605,
            10.800855984596765, 8.4768862207770468, 8.7709599753327296,
            8.5115699035032346, 6.5623254685786003, 4.577379648275234,
            4.8737227386601729, 4.8845566158386609, 4.9416124224116613,
            4.7068613038131062, 4.847774403441905, 3.641202640154293,
            4.865707211358564, 5.8317850326179617, 5.5646648097117852,
            5.8853513064217546, 6.6371132446435244, 7.1101839326107275,
            7.1871184922903826, 8.3465498527502113, 9.073611555861687,
            9.0870854024330132, 8.3398348638060895, 5.9142930450073328,
            6.4203717441697474, 7.2659339080090346, 7.2219849533674978,
            7.5313847774938836, 7.758637122587956, 7.6485459039247745,
            7.1610294883720007, 7.2388940990856998, 6.9341618895949626,
            6.6686421239842977, 5.2047658715621195, 2.6397003196912121,
            3.1091942507487307, 3.9894729532163118, 4.6656708461318193,
            4.5243402220041311, 5.1604522842264302, 5.3878571291789461,
            4.974325638270523, 4.4714657055103819, 3.9744830551350327,
            3.0170508042715429, 2.3489572154468794, 3.5151007572092858,
            4.0541939875749557, 4.1687462810245028, 4.2825289776537945,
            5.7083739657921253, 12.580634324230228, 16.397131049871689,
            19.065494398694895, 20.371646308861077, 19.941000225665718,
            20.204460151164653, 18.947481949383747, 16.459877952834979,
            11.294674261202355, 8.0265482410975864, 9.2898478040397627,
            11.14332904576645, 11.873670966563889, 12.684673166200744,
            13.797316164143426, 16.063193435096697, 15.897444378823213,
            15.397173477983268, 12.449335591374611]

    def test_standard_deviation_period_6(self):
        period = 6
        std = standard_deviation.standard_deviation(self.data, period)
        np.testing.assert_array_equal(std, self.std_period_6_expected)

    def test_standard_deviation_period_8(self):
        period = 8
        std = standard_deviation.standard_deviation(self.data, period)
        np.testing.assert_array_equal(std, self.std_period_8_expected)

    def test_standard_deviation_period_10(self):
        period = 10
        std = standard_deviation.standard_deviation(self.data, period)
        np.testing.assert_array_equal(std, self.std_period_10_expected)

    def test_standard_deviation_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            standard_deviation.standard_deviation(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)
