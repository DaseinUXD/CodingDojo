# == Schema Information
#
# Table name: users
#
#  created_at :datetime         not null
#  email      :string
#  first_name :string
#  id         :bigint(8)        not null, primary key
#  last_name  :string
#  updated_at :datetime         not null
#

class User < ApplicationRecord
end
