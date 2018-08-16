require_relative 'project' # include our Project class in our spec file
RSpec.describe Project do
  # FROM THE RGB ASSIGNMENT TAB/ASSIGNMENT
  it 'has a getter and setter for name attribute' do
    project      = Project.new
    project.name = "Name"
    expect(project.name).to eq("Name")
  end
  it 'has a getter and setter for the description attribute' do
    project             = Project.new
    project.description = "Description"
    expect(project.description).to eq("Description")
  end
  it 'has a method elevator_pitch to explain name and description' do
    project             = Project.new
    project.name        = "Name"
    project.description = "Description"
    expect(project.elevator_pitch).to eq("Name, Description")
  end
end
#
#
#
#
# FROM THE RED, GREEN, REFACTOR TAB/LESSON
# it "has a getter and setter for name attribute" do
#   project = Project.new
#   project.name = "Project Name"
#   expect(project.name).to eq("Project Name")
# end
#
#
# FROM THE METHOD TESTING TAB/ASSIGNMENT
# before(:each) do
#   @project1 = Project.new('Project 1', 'description 1', 'owner 1', 'tasks 1') # create a new project and make sure we can set the name attribute
#   @project2 = Project.new('Project 2', 'description 2', 'owner 2', 'tasks 2') # create a new project and make sure we can set the name attribute
# end
# it 'has a getter and setter for name attribute' do
#   @project1.name = "Changed Name" # this line would fail if our class did not have a setter method
#   expect(@project1.name).to eq("Changed Name") # this line would fail if we did not have a getter or if it did not change the name successfully in the previous line.
#   @project1.owner = "Changed Name" # this line would fail if our class did not have a setter method
#   expect(@project1.owner).to eq("Changed Name") # this line would fail if we did not have a getter or if it did not change the name successfully in the previous line.
# end
#
# it 'has a method elevator_pitch to explain name and description' do
#   expect(@project1.elevator_pitch).to eq("Project 1, description 1")
#   expect(@project2.elevator_pitch).to eq("Project 2, description 2")
# end
#
# it 'has a method add_tasks to push tasks into the tasks array' do
#   expect(@project1.add_tasks('task')).to eq ["task"]
# end

