class SurveyFormController < ApplicationController
  def result
    @result      = Result.create(name: params[:name], language: params[:language],
                                 location: params[:location],
                                 comments: params[:comments])
    @result_last = Result.last
    if flash.key?('count')
      flash[:count] = flash[:count] + 1
      @submit_count_many = "Thanks for submitting this form! You have submitted it #{flash[:count]} times now"
    else
      flash[:count] = 1
      @submit_count_0 = 'Thanks for submitting this form! This is the first time you submiited this form'
    end
  end

  def index
  end

  def reset
    flash[:count] = 0
    redirect_to '/'
  end
end
