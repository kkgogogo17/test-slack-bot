
modalView = {
	"title": {
		"type": "plain_text",
		"text": "My App",
		"emoji": True
	},
	"submit": {
		"type": "plain_text",
		"text": "Submit",
		"emoji": True
	},
	"type": "modal",
	"close": {
		"type": "plain_text",
		"text": "Cancel",
		"emoji": True
	},
	"blocks": [
		{
			"type": "section",
			"text": {
				"type": "plain_text",
				"text": ":wave: Hey!\n\nplease fill out the following form with information about the stale or missing product",
				"emoji": True
			}
		},
		{
			"type": "input",
			"block_id": "TeamInfluence",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Customers",
							"emoji": True
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Suppliers",
							"emoji": True
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Admins",
							"emoji": True
						},
						"value": "value-2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "My team",
							"emoji": True
						},
						"value": "value-3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Just me",
							"emoji": True
						},
						"value": "value-4"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Who's this an issue for",
				"emoji": True
			}
		},
		{
			"type": "input",
			"block_id": "Environment",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Production",
							"emoji": True
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Dev",
							"emoji": True
						},
						"value": "value-1"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Which environment?",
				"emoji": True
			}
		},
		{
			"type": "input",
			"block_id": "problemtype",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Customers can't access a findable SKU on Storefront",
							"emoji": True
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "Customers can't see all findable options on Storefront",
							"emoji": True
						},
						"value": "value-1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "I'm querying Product Cache and a SKU is missing",
							"emoji": True
						},
						"value": "value-2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "I'm querying Product Cache and a product's data is stale",
							"emoji": True
						},
						"value": "value-3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "None of the above(please provide more infor as a reply)",
							"emoji": True
						},
						"value": "value-4"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "What's the issue?",
				"emoji": True
			}
		},
		{
			"type": "input",
            "block_id": "brandCatalog",
			"element": {
				"type": "static_select",		
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "1-Wayfair US",
							"emoji": True
						},
						"value": "1"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "2-Wayfair UK",
							"emoji": True
						},
						"value": "2"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "3-Wayfair Germany",
							"emoji": True
						},
						"value": "3"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "4-Wayfair Australia",
							"emoji": True
						},
						"value": "4"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "5-Joss US",
							"emoji": True
						},
						"value": "5"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "6-Joss UK",
							"emoji": True
						},
						"value": "6"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "7-Joss Germany",
							"emoji": True
						},
						"value": "7"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "8-Joss Australia",
							"emoji": True
						},
						"value": "8"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "9-Joss France",
							"emoji": True
						},
						"value": "9"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "10-Wayfair Canada(English)",
							"emoji": True
						},
						"value": "10"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "11-Wayfair Canada (French)",
							"emoji": True
						},
						"value": "11"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "12-AllModern US",
							"emoji": True
						},
						"value": "12"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "13-Perigold US",
							"emoji": True
						},
						"value": "13"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "14-BirchLane US",
							"emoji": True
						},
						"value": "14"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "15-Original Data - US",
							"emoji": True
						},
						"value": "15"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "16-Original Data - UK",
							"emoji": True
						},
						"value": "16"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "17-Original Data - DE",
							"emoji": True
						},
						"value": "17"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "18-Arlow",
							"emoji": True
						},
						"value": "18"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "19-Wayfair Ireland",
							"emoji": True
						},
						"value": "19"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "20-Wayfair Austria",
							"emoji": True
						},
						"value": "20"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "21-AllModern Lynnfield MA (physical retail)",
							"emoji": True
						},
						"value": "21"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "22-Joss Burlington MA (physical retail)",
							"emoji": True
						},
						"value": "22"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "23-AllModern Dedham MA (physical retail)",
							"emoji": True
						},
						"value": "23"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Which brand catalog?",
				"emoji": True
			}
		},
		{
			"type": "input",
            "block_id": "SKUInput",
			"element": {
				"type": "plain_text_input",
				"multiline": True,
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": "List one impacted product sku.",
				"emoji": True
			}
		},
		{
			"type": "input",
            "block_id": "findable",
			"element": {
				"type": "static_select",
				"placeholder": {
					"type": "plain_text",
					"text": "Select an item",
					"emoji": True
				},
				"options": [
					{
						"text": {
							"type": "plain_text",
							"text": "Yes",
							"emoji": True
						},
						"value": "value-0"
					},
					{
						"text": {
							"type": "plain_text",
							"text": "No",
							"emoji": True
						},
						"value": "value-1"
					}
				],
				"action_id": "static_select-action"
			},
			"label": {
				"type": "plain_text",
				"text": "If an issue with accessing products on Storefront, have you already verified that the product (SKU or option) is findable?",
				"emoji": True
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": "If an issue with accessing products on Storefront, include a link to the relevant PDP or Browse URL(optional)",
				"emoji": True
			}
		},
		{
			"type": "input",
			"element": {
				"type": "plain_text_input",
				"multiline": True,
				"action_id": "plain_text_input-action"
			},
			"label": {
				"type": "plain_text",
				"text": "Do you have any more information about the issue you'd like to share?(optional)",
				"emoji": True
			}
		}
	]
}