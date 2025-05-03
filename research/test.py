from transformers import TrainingArguments
import transformers

print("Transformers version being used:", transformers.__version__)

print("Transformers loaded from:", transformers.__file__)

args = TrainingArguments(
    output_dir="test-output",
    num_train_epochs=1,
    per_device_train_batch_size=4,
    eval_strategy="epoch"
)

print(args.eval_strategy)