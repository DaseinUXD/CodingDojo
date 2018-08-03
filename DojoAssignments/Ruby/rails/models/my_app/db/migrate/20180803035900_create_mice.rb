class CreateMice < ActiveRecord::Migration[5.2]
  def change
    create_table :mice do |t|
      t.string :name
      t.integer :weight

      t.timestamps
    end
  end
end
