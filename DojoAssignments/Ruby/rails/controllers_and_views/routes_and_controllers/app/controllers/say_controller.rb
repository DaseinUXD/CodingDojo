class SayController < ApplicationController
  def index
    render plain: 'What do you want me to say????'
  end

  def hello
    render plain: 'Hello CodingDojo!'
  end

  def say_hello
    render plain: 'Saying Hello!'
  end

  def joe
    render plain: 'Saying Hello Joe!'
  end

  def michael
    redirect_to '/say/hello/joe'
  end

  def times
    if session.has_key?('count')
      session[:count] = session[:count] + 1
      render plain: "You visited this URL #{session[:count]} times"
    else session[:count] = 1
      render plain: "You have visited this URL #{session[:count]} times"
    end
    # render plain: 'You visited this URL '
  end

  def reset
    session[:count] = 0
    render plain: 'Destroyed the session!'
  end

end
