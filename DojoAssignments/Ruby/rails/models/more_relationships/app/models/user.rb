class User < ApplicationRecord
  has_one :account
  has_many :events
  has_many :attendees
  has_many :events_attending, through: :attendees, source: :event
end
