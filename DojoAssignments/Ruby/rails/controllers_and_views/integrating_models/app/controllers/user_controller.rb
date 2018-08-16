class UserController < ApplicationController
  def users
    # render plain: 'This rendered plain text in response to USERS'
    render json: User.all
  end

  def create
    @user = User.create(name: params[:name])
    redirect_to '/users/'
  end

  def new
  end

  def edit
    puts params
    # render plain: 'This rendered plain text is in response to EDIT'
    @user_edit = User.find_by(id: params[:id])
  end

  def total
    render json: User.count
  end

  def show_one
    puts params
    render json: User.find_by(id: params[:id])
  end


end
