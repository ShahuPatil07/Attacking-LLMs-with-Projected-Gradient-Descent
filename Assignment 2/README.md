### I tested 4 LLMs using Hugging Face. Prompt given by me was "IIT Bombay is one of the best institute". Prompt format for these LLMs was-
* from transformers import AutoTokenizer, LlamaForCausalLM

* model = LlamaForCausalLM.from_pretrained("model name")
* tokenizer = AutoTokenizer.from_pretrained("model name")
* prompt = "IIT Bombay is one of the best institute"
* inputs = tokenizer(prompt, return_tensors="pt")
* generate_ids = model.generate(inputs.input_ids, max_length=30)
* tokenizer.batch_decode(generate_ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]

# Outputs 

### openai-community/gpt2
 IIT Bombay is one of the best Institute of Social Sciences in India. It has a huge reputation and in this regard, I am pleased to mention it, as it is one of the most prestigious institutes of study in the country. I have heard that the President of the Institute is P.S. Narayanan who was born there.\n\nThis report is submitted as part of the ongoing inquiry and is submitted by an independent journalist to the Board of Directors of Bombay State Government. It

### lmsys/vicuna-7b-v1.5
 'IIT Bombay is one of the best Institute in India for Engineering and Technology. nobody can deny this fact. But the problem is that the placement record of IIT Bombay is not that good as compared to other IITs. The reason behind this is that the number of students appearing for placements is very high and the number of companies visiting IIT Bombay is limited.\n\nHowever, this does not mean that students of IIT Bombay are not'

