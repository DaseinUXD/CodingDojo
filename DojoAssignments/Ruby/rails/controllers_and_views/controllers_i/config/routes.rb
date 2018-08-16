Rails.application.routes.draw do
  get 'users/index'
  get 'users/new'
  get 'comments/index'
  get 'comments/new'
  get 'comments/edit'
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  resources :users
end
