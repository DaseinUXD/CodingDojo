Rails.application.routes.draw do
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  get 'users' => 'user#users'
  post 'users/users' => 'user#create'
  get 'users/new' => 'user#new'
  get 'users/:id/edit' => 'user#edit'
  get 'users/total' => 'user#total'
  get 'users/:id' => 'user#show_one'


end
