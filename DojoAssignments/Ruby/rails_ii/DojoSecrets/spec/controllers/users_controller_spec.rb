require 'rails_helper'

RSpec.describe UsersController, type: :controller do

  describe "GET #resources:users" do
    it "returns http success" do
      get :resources
      expect(response).to have_http_status(:success)
    end
  end

end
