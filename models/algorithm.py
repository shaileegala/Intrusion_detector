from math import sqrt
from scipy.stats import t


class TTests(object):

    @classmethod
    def t_statistic(cls, population_mean, sample_mean, sample_std_deviation, sample_length):
        """Gives the t_statistics

        :param population_mean: (float)
        :param sample_mean: (float)
        :param sample_std_deviation: (float)
        :param sample_length: (int)
        :return: (int) t_statistic
        """

        # Numerator is difference of sample mean and population mean
        t_num = float(sample_mean) - float(population_mean)

        # Denominator is sample's standard deviation divided by square root of sample length
        t_denom = float(sample_std_deviation)/sqrt(float(sample_length))

        return t_num/t_denom

    @classmethod
    def t_distribution(cls, sample_length, alpha):
        """

        :param sample_length: (int)
        :param alpha: (float)
        :return: (float, float) r_min, r_max
        """
        df = sample_length - 1
        half_alpha = alpha/float(2)

        # T-distribution minimum value
        r_min = t.ppf(half_alpha, df)

        # T-distribution maximum value
        r_max = t.ppf(1-half_alpha, df)

        return r_min, r_max


class Statistics(object):

    def __init__(self, data_list):

        self.data_list = data_list
        self.data_list_len_f = len(data_list)
        self.data_list_sum = sum(data_list)
        self.data_list_mean = None

    def mean(self):
        """

        :return: (float) mean value
        """
        if self.data_list_mean:
            return self.data_list_mean

        self.data_list_mean = self.data_list_sum/self.data_list_len_f
        return self.data_list_mean

    def variance(self):
        """

        :return: (float) variance value
        """
        mean = self.mean()

        square_diff = [(x-mean)^2 for x in self.data_list]
        return sum(square_diff)/self.data_list_len_f

    def standard_dev(self):
        """

        :return: (float) standard deviation
        """
        return sqrt(self.variance())

