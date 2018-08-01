arr = [3, 5, 1, 2, 7, 9, 8, 13, 25, 32]
puts arr.sum
ten_plus = [arr.reject { |i| i < 10 }]
puts ten_plus
puts arr.reject { |i| i < 10 }.sum

names = ['John', 'KB', 'Oliver', 'Matthew', 'Christopher']

# puts names.shuffle

puts names.reject { |i| i.length < 5 }

alphabet = %w[a b c d e f g h i j k l m n o p q r s t u v w x y z ]
puts alphabet.length
puts alphabet.shuffle
shuffle = alphabet.shuffle
puts '++++++++++++++'
puts shuffle.last
puts shuffle.first

if shuffle.first == 'a'
  puts 'This is a vowel'
else
puts 'Not a vowel'
end

# puts random
def random
  rand(55-100)
end
random_array = Array.new(10) {random}
puts random_array
puts '++++++++++++++++++++++++++'
puts random_array.sort_by { |i| i }
puts random_array.min
puts random_array.max


puts '}{}{}{}{}{}{}{}{}{}{}{}{}{'
five_rand_letters = (65+rand(26)).chr, (65+rand(26)).chr, (65+rand(26)).chr, (65+rand(26)).chr, (65+rand(26)).chr
letter_array = Array.new(10) {five_rand_letters}
print letter_array, ' :: '