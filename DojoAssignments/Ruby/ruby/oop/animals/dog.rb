require_relative 'mammal'
class Dog < Mammal
  def pet
    @health += 5
    self
  end
  def walk
    @health -= 1
    self
  end
  def run
    @health -= 10
    self
  end
end

Dog.new.walk.walk.walk.run.run.pet.display_health
fido = Dog.new
fido.walk.run.pet.pet.display_health
