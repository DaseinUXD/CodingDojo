# Print 1-255
def print_1_255
  # puts (1...255).each { |i| puts i }
  puts 1.upto(255) { |i| print i, ' :: ' }
end

print_1_255
# Print odd numbers between 1-255
def print_odd
  puts 1.upto(255).find_all { |i| (i % 3).zero? } #same same
  print (1..255).find_all { |i| (i % 3).zero? } #same same
end

print_odd
# Print Sum
def print_sum
  puts 0.upto(255) { |i| puts i }
  puts 0.upto(255) { |i| puts 'New number: %d, the  Sum: %d' % [i, (i + i)] }
end

print_sum
# Iterating through an array
def iterate_array x
  x.each { |i| print i, ', ' }
end

# iterate_array [1, 2, 3, 4, 5]
# Find Max
def find_max y
  print y.max
end

# find_max [2, 3, -6, 7, 99]
# Get Average

def get_average z
  z.each { |i| print (i + i) }
  
  # puts i/z.length
end

get_average [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Array with Odd Numbers

# Greater than Y

# Square the values

# Eliminate Negative Numbers

# Max, Min, and Average

# Shifting the Values in the Array

# Number to String
