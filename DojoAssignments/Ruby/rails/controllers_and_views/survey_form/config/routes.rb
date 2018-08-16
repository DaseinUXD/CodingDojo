Rails.application.routes.draw do
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  get '/' => 'survey_form#index'
  post 'result' => 'survey_form#result'
  get 'reset' => 'survey_form#reset'

end
