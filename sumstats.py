# Implement the following summary statistics functions. 
# Do not use `max`, `min`, the `statistics` library, or other
# pre-written solutions.

# Throughout this module, don't worry about edge cases. Specifically, don't worry about
# the following errors. If a user asks for an undefined value, too bad for them. 
#
# - `mean`, `median`, and `mode` are undefined when the list of values is 
#   empty. In practice, empty lists will sometimes cause errors like division 
#   by zero. 
# - `variance` and `standard_deviation` are undefined when there are fewer than
#   two values, because then there's no spread. 

def mean(values):
    """Retuns the mean (average) of the values."""

def median(values):
    """Returns the median of the values, or the number in the central position
    when sorted. If there are an even number of values, returns the average of the 
    two central values."""

def mode(values):
    """Returns the mode of the values. The mode is the most common value. If there
    are multiple modes, thus function returns one of them but provides no guarantee as to
    which mode will be returned.
    """

def variance(values):
    """Returns the (sample) variance of the values, or the average squard amount by which values
    differ from the mean. Variance is a measure of spread: a higher variance means the values 
    are more spread out on average. 

    To compute the variance, first find the mean of the values. Then, for each value, 
    find the squared difference between the value and the mean. Sum these squared differences
    and divide by (n-1), where n is the number of values. 

    Because variance is a measure of spread, it doesn't make sense to talk about the variance
    when there are fewer than two values. 
    """

def standard_deviation(values):
    """Returns the (sample) standard deviation, or the average amount by which values differ
    from the mean. Although variance is used for its nice mathematical properties, standard deviation
    provides a better description because it's in the same units as the values. 

    The standard deviation is just the square root of the variance. You may use `math.sqrt`
    to find the standard deviation. 
    """
