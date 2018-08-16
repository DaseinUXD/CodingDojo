require 'test_helper'

class SurveyFormControllerTest < ActionDispatch::IntegrationTest
  test "should get result" do
    get survey_form_result_url
    assert_response :success
  end

end
