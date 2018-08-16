# frozen_string_literal: true

class DojoController < ApplicationController
  skip_before_action :verify_authenticity_token
  # protect_from_forgery prepend: true, with: :exception
  # before_action :authenticate_user!
  # before_action :set_bug, only: [:show, :edit, :update]

  # /, dojo, index
  def index
    @dojos_all = Dojo.all

  end

  # new
  def new
  end

  # create
  def create
    @dojo        = Dojo.create(branch: params[:branch], street: params[:street],
                               city:   params[:city], state: params[:state])
    @error_count = @dojo.errors.count
    if @error_count.zero?
      flash[:success] = 'Success! You added a new Coding Dojo Branch'
      redirect_to @dojo
    else
      puts 'the error count is:', @error_count
      @error_messages = @dojo.errors.full_messages
      puts @error_messages
      render 'new'
    end
  end

  # show
  def show
    @dojo = Dojo.find_by(id: params[:id])
    puts @dojo.id


  end

  # edit
  def edit
    @dojo = Dojo.find_by(id: params[:id])
    # dojo  = Dojo.find_by(id: params[:id])
    # puts dojo
  end

  # update
  def update
    dojo = Dojo.find_by(id: params[:id])
    # dojo = Dojo.find_by(id: params[:id])
    dojo.update(branch: params[:branch], street: params[:street],
                city:   params[:city], state: params[:state])
    # Dojo.save
    # puts @dojo.branch
    redirect_to '/index'
  end

  # destroy
  def destroy

    @dojo = Dojo.find_by(id: params[:id])
    puts @dojo.street, @dojo.city
    @dojo.destroy
    puts 'Dojo Destroyed'
    redirect_to '/'
  end
end
