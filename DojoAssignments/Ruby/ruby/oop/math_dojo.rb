class MathDojo
  attr_accessor :sum, :difference, :total
  
  def initialize
    # @result = result
    @total      = 0

    self
  
  end
  
  
  def add (*x)
    for i in 0...x.length
      if x[i].is_a?(Array)
        @total += x[i].sum
      else
        @total += x[i]
      end
    end
    self
  end
  
  
  def subtract (*x)
    for i in 0...x.length
      if x[i].is_a?(Array)
        @total -= x[i].sum
      else
        @total -= x[i]
      end
    end
    self
  
  end
  
  def result
    puts "#{@total}"
  end

end

challenge0 = MathDojo.new.add(2).result # => 2
challenge1 = MathDojo.new.add(2).add(2, 5).result # => 9
challenge2 = MathDojo.new.add(2).add(2, 5).subtract(3, 2).result # => 4
challenge3 = MathDojo.new.add(1).add([3, 5, 7, 8], [2, 4.3, 1.25]).subtract([2, 3], [1.1, 2.3]).result # => 23.15
puts challenge0
puts challenge1
puts challenge2
puts challenge3
