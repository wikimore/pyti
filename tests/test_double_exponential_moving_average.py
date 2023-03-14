import unittest
import numpy as np

from tests.sample_data import SampleData
from pyti import double_exponential_moving_average


class TestDoubleExponentialMovingAverage(unittest.TestCase):
    def setUp(self):
        """Create data to use for testing."""
        self.data = SampleData().get_sample_close_data()

        self.dema_period_6_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
            np.nan, np.nan, np.nan, np.nan, np.nan, 814.39826450317082,
            816.66267593402222, 816.38407384631512, 811.89757651064974,
            810.32809027203473, 801.76291196016223, 794.50933589751924,
            782.07121905153599, 776.60751674776918, 766.88608489820399,
            761.63998332305869, 766.46362391898549, 777.37149879972458,
            782.76352759497718, 782.47184436374596, 782.2239300622291,
            785.03026118164371, 785.57312373950936, 780.08438277009554,
            782.82199149512974, 781.43161360300553, 778.05182650622203,
            763.69914326178434, 765.80970755684461, 772.60604659225692,
            790.00070134560258, 804.0019799930119, 806.54380897254123,
            797.16966250809605, 790.47384727414942, 789.2811173735422,
            796.48053300712138, 802.995360035884, 812.85803428109296,
            818.50882806250695, 823.79618020316457, 829.4670109031548,
            835.13194057239514, 831.31352150929058, 826.85687184590211,
            827.36088583505591, 824.28366731657684, 814.10953047160353,
            806.75616044795288, 803.33671667688213, 806.07475585686154,
            806.43244712563489, 809.77458333158086, 805.29046766176248,
            804.02101341198693, 802.27445540049564, 801.67730126181652,
            800.25397860921942, 801.28836253983752, 802.08404696091009,
            806.46908016463715, 809.46152107684054, 806.51474972455333,
            811.59983231040587, 814.74318359431447, 810.5021498205997,
            804.56126448751058, 798.72094801604067, 797.40800658462808,
            797.86923695825158, 792.44025463626247, 789.26611669743227,
            793.49070457334517, 790.62858411799039, 796.74447937620096,
            802.96378899943818, 807.15458667235032, 803.26711490375749,
            797.12139732796595, 793.29320250915339, 791.33482308547048,
            792.25173080721731, 791.63491615181943, 791.11244091352569,
            792.45499916489894, 794.97145198187047, 796.42637740204191,
            798.42823251281766, 801.37741485558229, 804.55112456243887,
            803.75094361303002, 805.5761906287737, 807.10857305849322,
            808.34295633962108, 808.93471737971515, 808.49869223433791,
            807.22159861880073, 807.06427062511352, 801.59668233540901,
            799.33686878847493, 798.82152839022694, 799.19709016757542,
            794.4038205941572, 777.59862297519658, 766.58111600749953,
            758.15441732143881, 753.73263212184338, 752.77383668964967,
            750.77025286250284, 753.0519066903139, 752.70863015856708,
            752.67430493318409, 742.96415869574696, 737.36036041788009,
            731.16477683930816, 729.40308865220493, 726.08835468423422,
            719.3576110696365, 711.09522540775777, 707.50687400227309,
            703.93652605888281, 704.95928675610264]

        self.dema_period_8_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
            np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
            811.52966005039048, 803.81856064257602, 797.26005628251721,
            786.33901317417588, 779.8924674747924, 769.69132696276597,
            763.40905505598482, 765.26785709163437, 772.93574157458568,
            777.50300183967363, 778.35420481368624, 779.19626388154938,
            782.22580384905245, 784.7541727175377, 782.25854853473902,
            784.34134498691515, 782.18204973339107, 778.80180643300446,
            767.05409005201557, 767.65126161777368, 771.73808057337124,
            785.99021181146122, 798.88896277809829, 802.32440630243593,
            795.31855688072005, 791.10396300250704, 792.00774139543887,
            798.99009272965623, 805.01990428365082, 811.89692940086377,
            815.13893716594748, 819.86665975165306, 826.7938731165608,
            834.18275214847324, 833.15731395827743, 830.1067264123958,
            830.06999651928345, 826.88681875207988, 818.26084326481805,
            811.26446443027453, 806.20990683067964, 806.20331074495027,
            806.1709917128876, 808.54021703683816, 803.97407877119895,
            802.43697769134235, 801.4864087660925, 801.69959718464963,
            800.80476460146554, 801.46275863910751, 801.46084143679775,
            804.59604725178849, 807.73945944373679, 806.01681557748077,
            810.40570640552346, 813.62858625475633, 810.91406285604785,
            806.42592783525311, 801.48999541892613, 798.97280329805233,
            798.84992431256455, 794.50841091198299, 790.29093562901653,
            792.1748760597734, 789.61379280800486, 794.7211075958694,
            800.73270766514997, 804.57714906619083, 801.8915743238224,
            798.12579029399683, 794.88107938817529, 793.04626550414389,
            794.15437954166464, 792.98824833812569, 791.19241887379678,
            791.17023442536322, 793.20902261259084, 795.0577262080933,
            797.55312164419058, 800.42504351894559, 803.26359280783913,
            803.30822339186739, 805.43563722296597, 807.08152014238897,
            808.41755281167627, 809.31878054486174, 809.22804924753427,
            807.92184414501992, 807.62804922397788, 803.31440459989881,
            800.9251144942782, 799.8847402775267, 799.59558771151296,
            795.19970694562699, 781.02517906706305, 770.13910528470001,
            761.18181473135087, 756.09015706438572, 753.81923875665939,
            750.51252832162936, 749.9015546304671, 748.77807000378118,
            749.56175042068935, 742.52199884387528, 738.19780817704032,
            732.62207257454384, 730.34365707829238, 726.9291965231215,
            720.50393870832931, 711.97005292741403, 707.39046480291142,
            703.81250108317442, 704.10057599918775]

        self.dema_period_10_expected = [np.nan, np.nan, np.nan, np.nan, np.nan,
            np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan,
            np.nan, np.nan, np.nan, np.nan, 783.19627971958187, 773.71120107133811,
            766.79783341359359, 766.38213675650843, 771.67412869849227,
            774.78853007908629, 775.08384518514617, 775.65968951306922,
            778.57590975540575, 781.33362662343347, 779.84746723491151,
            783.14619824577301, 783.07813745033911, 780.54742736548326,
            769.79018520771876, 769.18535115445422, 772.31790279381653,
            784.23248244657805, 795.01813689713231, 799.05236263337815,
            794.36738929723538, 790.75288627304076, 790.688879355258,
            797.19696858572308, 804.43255522849915, 812.19116313650227,
            816.37175031439972, 819.83138323476874, 824.36563607216749,
            830.69500546817824, 831.63489635531835, 831.01309871996193,
            832.03194285009181, 829.66371546694029, 822.13164909404588,
            815.34369831864615, 810.39085698579322, 809.56609611008253,
            807.98821823136257, 808.42930600167995, 804.43539283341158,
            802.69013593400427, 800.63681883373613, 800.15611968725977,
            799.69299779483288, 800.88426456238096, 801.26626573907481,
            804.00094129804427, 806.36993547311533, 804.83492487621584,
            808.96533681764151, 812.16694643903486, 810.38256156856846,
            806.94838985368494, 802.86860706128118, 800.69677578735264,
            800.44667755501098, 795.91856959231632, 792.03881667367295,
            793.5046791785453, 790.22936540189494, 793.364588916348,
            798.22231705041099, 802.04200621762118, 800.79313492988877,
            797.64757027402334, 794.60862507676165, 793.67779025959612,
            794.52321593547811, 793.68710154857206, 792.84294121868152,
            792.42681677474513, 793.08710879383341, 793.7945747704066,
            795.90398004164638, 798.84640010709654, 802.00131519583226,
            802.53061491178551, 804.45525774408736, 806.30874204756128,
            808.08480414831604, 809.26129601553021, 809.48687914712661,
            808.69171334395105, 808.55716309996399, 804.63620443419359,
            802.2907151689044, 801.26501213335587, 800.64117550277854,
            796.58948601022394, 784.08972939150783, 773.69623171866681,
            764.81832780045931, 758.73792907578024, 755.25570832271728,
            751.69978491186259, 750.36599903623755, 748.29322295260533,
            746.99186066438847, 740.18128477470884, 736.70420713478666,
            732.13303337040861, 730.30687926052337, 727.14864908037202,
            721.40060492285465, 713.69772901661167, 708.85437042796104,
            704.24968239602902, 703.21383054756723]

    def test_double_exponential_moving_average_period_6(self):
        period = 6
        dema = double_exponential_moving_average.double_exponential_moving_average(self.data, period)
        np.testing.assert_array_equal(dema, self.dema_period_6_expected)

    def test_double_exponential_moving_average_period_8(self):
        period = 8
        dema = double_exponential_moving_average.double_exponential_moving_average(self.data, period)
        np.testing.assert_array_equal(dema, self.dema_period_8_expected)

    def test_double_exponential_moving_average_period_10(self):
        period = 10
        dema = double_exponential_moving_average.double_exponential_moving_average(self.data, period)
        np.testing.assert_array_equal(dema, self.dema_period_10_expected)

    def test_double_exponential_moving_average_invalid_period(self):
        period = 128
        with self.assertRaises(Exception) as cm:
            double_exponential_moving_average.double_exponential_moving_average(self.data, period)
        expected = "Error: data_len < period"
        self.assertEqual(str(cm.exception), expected)
