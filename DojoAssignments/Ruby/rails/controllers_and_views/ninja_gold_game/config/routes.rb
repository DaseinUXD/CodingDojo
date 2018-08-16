Rails.application.routes.draw do
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  get '/' => 'rpg#index'
  get 'farm' => 'rpg#farm'
  get 'cave' => 'rpg#cave'
  get 'casino' => 'rpg#casino'
  get 'house' => 'rpg#house'
end
