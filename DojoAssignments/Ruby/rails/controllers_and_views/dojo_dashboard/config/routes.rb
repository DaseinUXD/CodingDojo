Rails.application.routes.draw do
  get 'dojo/:dojo_id/students' => 'students#index' # A page that displays all students for a specific dojo
  get 'dojo/:dojo_id/students/new' => 'students#new' # A page with a form to create a new student belonging to a specific dojo
  post 'dojo/:dojo_id/students' => 'students#create' # A URL that process the information submitted from the page to create a new student
  get 'dojo/:dojo_id/students/:id' => 'students#show' # A page that displays a specific student's profile page
  get 'dojo/:dojo_id/students/:id/edit' => 'students#edit' # A page with a form to edit a specific student
  patch 'dojo/:dojo_id/students/:id' => 'students#update' # A URL that process the information submitted from the page to edit a student
  delete 'dojo/:dojo_id/students/:id' => 'students#destroy' # Delete a specific student
  get '/' => 'dojo#index'
  get 'index' => 'dojo#index'
  get 'dojo' => 'dojo#index'
  get 'dojo/new' => 'dojo#new'
  post 'dojo' => 'dojo#create'
  get 'dojo/:id' => 'dojo#show'
  get 'dojo/:id/edit' => 'dojo#edit'
  patch 'dojo/:id' => 'dojo#update'
  delete 'dojo/:id' => 'dojo#destroy'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
