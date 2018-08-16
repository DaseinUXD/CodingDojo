require 'rails_helper'

RSpec.describe User, type: :model do
  # THIS IS THE CONTROL
  context "With valid attributes" do
    it "should save" do
      user = User.new(first_name: 's', last_name: 'chang', email: 's@mail.com')
      expect(user).to be_valid
    end
  end
  context "with invalid attributes" do
    it "should not save if first_name field is blank" do
      user = User.new(
          first_name: '',
          last_name:  'chang',
          email:      's@mail.com')
      expect(user).to be_invalid
    end
    it "should not save if last_name field is blank" do
      user = User.new(
          first_name: 's',
          last_name:  '',
          email:      's@mail.com')
      expect(user).to be_invalid
    end


    it "should not save if email already exists" do
      user1 = User.new(
          first_name: 's',
          last_name:  'chang',
          email:      's@mail.com')
      user1.save
      user2 = User.new(
          first_name: 's',
          last_name:  'chang',
          email:      's@mail.com')
      expect(user2).to be_invalid
    end


    it "should not save if invalid email format" do
      user = User.new(
          first_name: 's',
          last_name:  'chang',
          email:      'sn.com')
      expect(user).to be_invalid
    end

  end

end
