from selenium import webdriver
import json

class DynamicePageCheck(object):
	
	def __init__(self, url):
		self.driver = webdriver.Chrome()
		self.driver.get(url)
		with open('xpath.json', 'r') as f:
			self.data = json.load(f)

	def get_elements(self, xpath, tag_name):
		return self.driver.find_element_by_xpath(xpath).\
				find_elements_by_tag_name(tag_name)

	def get_element_text(self, xpath):
		return self.driver.find_element_by_xpath(xpath).text


	def get_attribute(self, xpath, attr):
		return self.driver.find_element_by_xpath(xpath).get_attribute(attr)

	def get_element(self, xpath):
		return self.driver.find_element_by_xpath(xpath)

	def get_tracking_page_info(self):
		tab_text = [el.text for el in self.get_elements(self.data['TRACK_TRACE_PAGE']['TAB_TEXT']), 'li']
		text_field_placeholoder = self.get_element(self.data['TRACK_TRACE_PAGE']['TEXT_FIELD']).find_elements_by_tag_name('input')[-1].\
									get_attribute('placeholder')
		btn_for_search = self.get_element(self.data['TRACK_TRACE_PAGE']['SEARCH_BUTTON'])
		btn_text = btn_for_search.text
		btn_loading_text = self.get_attribute(self.data['TRACK_TRACE_PAGE']['SEARCH_BUTTON'])
		ref_no_url = self.get_attribute(self.data['TRACK_TRACE_PAGE']['BY_REF_TAB'])

		placeholder_url = []
		placeholder_url.append(btn_loading_text)
		placeholder_url.append(ref_no_url)

		search_btn = []
		search_btn.append(btn_text)
		search_btn.append(btn_loading_text)

		return {
			"tab_text": tab_text,
			"tf_placeholder_ref_url": placeholder_url,
			"search_btn": search_btn
		}

	@property
	def track_and_trace_page_info(self):
		return mapping_resource.CELL_SPLIT_TOKEN.join(self.get_tracking_page_info['tab_text']) \
				+ mapping_resource.ROW_SPLIT_TOKEN \
				+ mapping_resource.CELL_SPLIT_TOKEN.join(self.get_tracking_page_info['tf_placeholder_ref_url']) \
				+ mapping_resource.ROW_SPLIT_TOKEN \
				+ mmapping_resource.CELL_SPLIT_TOKEN.join(self.get_tracking_page_info['search_btn'])

	def get_text_and_placeholder(self, element):
		if not element is None:
			div_text = element.text
			try:
				div_placeholder = element.find_elements_by_tag_name('input')[0].get_attribute('placeholder')
				print(div_placeholder)
			except:
				div_placeholder = ''

			return [div_text, div_placeholder]
		else:
			return []


	def get_transmit_time_page_info(self):
		form_data = []
		form_data.append(self.get_element_text(self.data['TRANSMIT_TIME_PAGE']['TAB_TITLE']))
		form_data.append(self.get_element_text(self.data['TRANSMIT_TIME_PAGE']['PROMOTION_LINK']))
		form_data.append(self.get_attribute(self.data['TRANSMIT_TIME_PAGE']['PROMOTION_LINK'], 'href'))

		print(form_data)

		for el in self.get_elements(self.data['TRANSMIT_TIME_PAGE']['FORM_DATA'], 'dl'):
			form_data.append(self.get_text_and_placeholder(el))

		search_btn = self.get_element(self.data['TRANSMIT_TIME_PAGE']['SEARCH_BUTTON'])
		form_data.append()

		return form_data

	def tax_query_page_info(self):
		way_bill_el = self.get_element(self.data['TAX_QUERY_PAGE']['BILL_NUMBER_INPUT'])
		way_bill_title = way_bill_el.text
		way_bill_placeholder = way_bill_el.find_element_by_tag_name('input').get_attribute('placeholder')

		verification_el = self.get_element(self.data['TAX_QUERY_PAGE']['VERIFY_CODE_INPUT'])
		verification_title = verification_el.text
		verification_placeholder = verification_el.find_element_by_tag_name('input').get_attribute('placeholder')


	def import_export_page_info(self):
		_page_info = []

		for el in self.driver.find_elements_by_class_name('form-group'):

			try:
				label = el.find_elements_by_tag_name('label')
			except:
				label = []

			try:
				drop_list = el.find_elements_by_tag_name('button')
			except:
				drop_list = []


			try:
				input_field = el.find_elements_by_tag_name('input')
			except:
				input_field = []

			if len(label) == 2:
				if len(drop_list) == 2:
					_page_info.append(label[0].text)
					_page_info.append(drop_list[0].text)
					_page_info.append(label[1])
					_page_info.append(drop_list[1])
				elif len(input_field) == 2:
					_page_info.append(label[0].text)
					_page_info.append(input_field[0].get_attribute('placeholder'))
					_page_info.append(label[1].text)
					_page_info.append(input_field[1].get_attribute('placeholder'))
				elif len(input_field) == 1 and len(drop_list) == 1:
					_page_info.append(label[0].text)
					_page_info.append(drop_list[0].text)
					_page_info.append(label[1].text)
					_page_info.append(input_field[0].get_attribute('placeholder'))

		return _page_info


	def close(self):
		self.driver.quit()


xx = DynamicePageCheck('http://www.sf-express.com/kr/en/dynamic_function/clearance/restricted_delivery/')

print(xx.import_export_page_info())
