class Project
  attr_accessor :name, :description

  def initialize
    @name        = name
    @description = description

  end

  def elevator_pitch
    "#{@name}, #{@description}"

  end

  # attr_accessor :name
  # def name(name)
  #   @name = name
  # end
  # def name
  #   @name
  # end
  #

  # FROM THE METHOD TESTING TAB/ASSIGNMENT
  # attr_accessor :name, :description, :owner
  # def initialize name, description, owner, tasks
  #   @name = name
  #   @description = description
  #   @owner = owner
  #   @tasks = []
  # end
  # def add_tasks(task)
  #   @tasks.push(task)
  # end
  # def elevator_pitch
  #   "#{@name}, #{@description}"
  # end
end
