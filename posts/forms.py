from django import forms

from posts.models import Comment, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["image", "text"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].widget.attrs.update({"placeholder": "Добавьте подпись..."})
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "comment-box"
            visible.label = ""


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            "text",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["text"].widget.attrs.update(
            {"placeholder": "Добавьте комментарий...", "rows": "1"}
        )
        for visible in self.visible_fields():
            visible.field.widget.attrs["class"] = "comment-box"
            visible.label = ""
