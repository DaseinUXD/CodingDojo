class User < ApplicationRecord
  has_many :friends, foreign_key: :friend_id, class_name: 'Friendship'
  has_many :friends_with, through: :friends, source: :friend

  has_many :friends_of, foreign_key: :user_id, class_name: 'Friendship'
  has_many :befriended_by, through: :friends_of, source: :befriended
end
