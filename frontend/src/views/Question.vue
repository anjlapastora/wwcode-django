<template>
    <div class="single-question mt-2">
        <div class="container">
            <h1>{{ question.content }}</h1>
            <p class="mb-0">Posted by:
                <span class="author-name">{{ question.author }}</span>
            </p>
            <p>{{ question.created_at }}</p>
        </div>
    </div>
</template>

<script>
import { apiService } from "../common/api.service.js"
export default {
    name: "Question",
    props: {
        slug: {
            type: String,
            required: true
        }
    },
    data() {
        return {
            question: {}
        }
    },
    methods: {
      setPageTitle(title) {
          document.title = title;

      },
      getQuestionData() {
          let endpoint = `/api/questions/${this.slug}/`;
          apiService(endpoint)
            .then(data => {
                this.question = data;
                this.setPageTitle(data.content)
            })
      }
    },
    created() {
        this.getQuestionData(),
        console.log(this.question);
    }
}
</script>

<style scoped>
  .question-author {
    font-weight: bold;
    color: #DC3545;
  }
  .question-link {
    font-weight: bold;
    color: black;
  }
  .question-link:hover {
    color: #343A40;
    text-decoration: none;
  }
</style>