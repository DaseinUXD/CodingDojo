players = Player.all
players.each do |player|
  puts player.team.name
  puts player.team.mascot
  puts player.team.stadium
end

players = Player.includes(:team)
players.each do |player|
  puts player.team.name
  puts player.team.mascot
  puts player.team.stadium
end

players = Player.includes(:team).where("teams.name ='Chicago Bulls'").references(:team)
players = Player.includes(:team).where("teams.stadium ='Staples Center'").references(:team)
teams = Team.includes(:players).where("player.name LIKE :prefix", prefix: "#{Z}%")
