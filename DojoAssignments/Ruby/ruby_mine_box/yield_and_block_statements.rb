def test
  puts 'You are in the method'
  yield
  puts 'You are again back to the method'
  yield
end

test { puts 'You are in the BLOCK' }

def test_0
  yield 5
  puts "You are in the method test 0"
  yield 100
end

# test_0 { puts 'You are in the BLOCK' }
#
test_0 { |i| puts "You are in the block #{i}" }

arr =  Array.new(3)
puts arr.nil?
puts arr.length

