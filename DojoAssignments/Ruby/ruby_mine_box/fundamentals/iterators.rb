# * .any? { |obj| block } => true or false
# e.g. ["ant", "bear", "cat"].any? { |word| word.length >= 3 } # => true
animals = Array['ant', 'bear', 'cat'].any? { |word| word.length >= 3 }
puts animals
# .each => calls block once for each element in ruby self,
# passing that element as a block parameter.
# e.g. ["ant", "bear", "cat"].each { |word| print word, "--" }
#  => ant--bear--cat--
each_animal = Array['ant', 'bear', 'cat'].each { |word| print word, '--' }
puts each_animal
# .collect { |obj| block } => returns a new array with the results of running
# block once for every element in enum
#     e.g. (1..4).collect { |i| i*i } # => [1, 4, 9, 16]
#     e.g. (1..4).collect { "cat" } # => ["cat", "cat", "cat", "cat"]
collect = (1..4).collect { |i| i * i }
puts collect
# .detect/.find => returns the first for which block is not false.
#     e.g. (1..10).detect { |i| i %5 == 0 and i % 7 == 0 } # => nil
#     e.g. (1..100).detect { |i| i %5 == 0 and i % 7 == 0 } # => 35
detect  = (1..10).detect { |i| (i % 5).zero? && (i % 7).zero? }
detect2 = (1..100).detect { |i| (i % 5).zero? && (i % 7).zero? }
puts detect
puts detect2

# .find_all { |obj| block } or .select { |obj| block } => returns an array
# containing all elements of enum for which block is not false
#     e.g. (1..10).find_all { |i| i % 3 == 0 } # => [3, 6, 9]
find_all = (1..10).find_all { |i| (i % 3).zero? }
puts find_all
# .reject { |obj| block } => opposite of find_all
#     e.g. (1..10).reject { |i| i % 3 == 0 } # => [1, 2, 4, 5, 7, 8, 10]
reject = (1..10).reject { |i| (i % 3).zero? }
puts reject
# .upto(limit) => iterates block up to the int number
#     e.g. 5.upto(10) { |i| print i, " " } # => 5 6 7 8 9 10
upto_limit = 5.upto(10) { |i| print i, " " }
puts upto_limit
