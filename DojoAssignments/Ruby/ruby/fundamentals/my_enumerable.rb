module MyEnumerable
  def my_each
    # your code here!
    for i in self
      # puts self.length
       puts self
    end
  end
end
class Array
  include MyEnumerable
end
puts [1, 2, 3, 4].my_each { |i| puts i } # => 1 2 3 4

puts [1, 2, 3, 4].my_each  { |i| puts i * 10 } # => 10 20 30 40
# [1, 2, 3, 4].my_each { |i| puts i * 10 } # => 10 20 30 40
