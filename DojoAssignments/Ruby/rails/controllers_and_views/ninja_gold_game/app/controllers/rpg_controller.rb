class RpgController < ApplicationController
  def index
    unless session.key?('activity')
      session[:activity] = []
    end
  end

  def farm
    @farm_gold = rand(10..20)
    sum(@farm_gold)
    session[:activity] << ['text-success', "You earned #{@farm_gold} gold working on the farm!"]
    redirect_to '/'
  end

  def cave
    @cave_gold = rand(5..10)
    sum(@cave_gold)
    session[:activity] << ['text-success', "You mind #{@cave_gold} gold out of the cave!"]
    redirect_to '/'
  end

  def casino
    @casino_gold = rand(-50..50)
    sum(@casino_gold)
    if @casino_gold < 0
      session[:activity] << ['text-danger', "You entered a casino and you lost #{@casino_gold} gold from the casino!"]
      redirect_to '/'
    else
      session[:activity] << ['text-success', "You entered a casino and you won #{@casino_gold} gold from the casino!"]
      redirect_to '/'
    end
  end

  def house
    @house_gold = rand(2..5)
    sum(@house_gold)
    session[:activity] << ['text-success', "You found #{@house_gold} gold between the couch cushions at your house!"]
    redirect_to '/'
  end

  def sum(gold)
    if session.key?('gold_count')
      session[:gold_count] = session[:gold_count] + gold
    else
      session[:gold_count] = gold
    end
  end
end
