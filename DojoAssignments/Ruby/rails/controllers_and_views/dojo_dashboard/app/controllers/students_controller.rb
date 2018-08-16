# frozen_string_literal: true

class StudentsController < ApplicationController
  skip_before_action :verify_authenticity_token
  # student index
  def index
    dojo_id = params['dojo_id']
    @students = Dojo.find(dojo_id).students
    @dojo = Dojo.find(dojo_id)
  end

  # new student form
  def new
    @dojos = Dojo.all
    dojo_id = params['dojo_id']
    @dojo = Dojo.find(dojo_id)


  end

  # student
  def create
    @dojos = Dojo.all
    dojo_id = params['dojo_id']
    @dojo = Dojo.find(dojo_id)

    student = Student.create(first_name: params[:first_name],
                              last_name:  params[:last_name],
                              email:      params[:email],
                              dojo_id:    params[:dojo_select])
    selected_dojo = params[:dojo_select]

    # puts student.first_name
    # puts student.dojo_id
    # puts 'created new student in dojo ID:'


    @errors = student.errors.full_messages
    if @errors.count.zero?
      redirect_to "/dojo/#{selected_dojo}/students"
    else
      render 'new'
    end
    # if @error_count.zero?
    #   flash[:success] = 'Success! You added a new Coding Dojo Branch'
    #   redirect_to @dojo
    # else
    #   puts 'the error count is:', @error_count
    #   @error_messages = @dojo.errors.full_messages
    #   puts @errors.count

  end

  def show;
  end

  def edit;
  end

  def update;
  end

  def destroy;
  end
end
