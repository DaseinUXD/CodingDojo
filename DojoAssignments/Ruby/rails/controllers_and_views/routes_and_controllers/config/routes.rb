Rails.application.routes.draw do
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  get 'hello' => 'say#hello'
  get 'say/hello' => 'say#say_hello'
  get 'say/hello/joe' => 'say#joe'
  get 'say/hello/michael' => 'say#michael'
  get '/' => 'say#index'
  get 'times' => 'say#times'
  get 'times/reset' => 'say#reset'
end
