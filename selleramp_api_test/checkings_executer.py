from deepdiff import DeepDiff
import Constants

class BaseChecker(object):
    pass


class StatusCheck(BaseChecker):
    def __init__(self, status_to_check, expected_status):

        self.status_to_check = status_to_check
        self.expected_status = expected_status

    def execute(self):
        if self.status_to_check == self.expected_status:
            return True
        else:
            return("Actual endpoint status {} is not equal to expected status {}"
                   .format(self.status_to_check, self.expected_status))

class RequestResponseCompare(BaseChecker):
    def __init__(self, request_response_to_compare, additional_text=None, ignore_order_value=False):
        self.request_response_to_compare = request_response_to_compare
        self.additional_text = additional_text
        self.ignore_order_value = ignore_order_value


    def execute(self):
        value_to_check = self.request_response_to_compare
        result = ""
        for i in range(len(value_to_check)):
            difference = str(DeepDiff(value_to_check[0], value_to_check[1], ignore_order=self.ignore_order_value))
            if difference == '{}': #this means that there are no difference
                continue
            else:
                result = result + self.additional_text[i] + difference if self.additional_text \
                    else result + Constants.ApiConst.DEFAULT_TEST_NAME_FOR_COMPARE_RESPONSE + difference
        if result == "":
            result = True
        return result

class CheckingPerformer():

    def __init__(self, tests_to_execute):
        self.tests_to_execute = tests_to_execute

    def add(self, test_to_execute):
        self.tests_to_execute.append(test_to_execute)

    def run(self):
        checking_results = []
        for i in self.tests_to_execute:
            result = i.execute()
            checking_results.append(result)
        return checking_results

    def execute(self):
        checking_results = self.run()
        what_the_result = list(set(checking_results))
        if what_the_result[0] == True and len(what_the_result) == 1:
            checking_results = True
        # In case if there are other then True results for checking_result, then all errors would be concatenated into
        # a single one
        else:
            error = ""
            checking_results = list(filter(lambda x: x != True, checking_results))
            for i in checking_results:
                error += i
            checking_results = error

        return checking_results








