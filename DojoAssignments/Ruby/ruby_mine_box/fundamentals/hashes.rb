a = { :first_name => 'Coding', :last_name => 'Dojo' }
puts a
puts a['first_name'], a['last_name']

y = { first_name: 'Coding', last_name: 'Dojo' }
x = { 'first_name' => 'Coding', 'last_name' => 'Dojo' } # this one works!!!
# puts y
# puts y['first_name'], y['last_name']
# puts "Your last name is Dojo" if y['last_name'].eql? "Dojo"
puts x
puts x['first_name'], x['last_name']
puts "Your last name is Dojo" if x['last_name'].eql? "Dojo"

