<template>
    <div class="col-sm-12">
        <div class="row">
           <form class="form-inline">
            <div class="form-group col-md-3">
                <label>Search by Title</label>
                <button type="buttom" class="btn btn-primary btn-xs pull-right" @click="title_search=''">Clear</button>
                <multiselect v-model="title_search" :options="filtered_titles" :showLabels="false" @search-change="title_search_change">
                    <span slot="noResult">{{noResult}}</span>
                </multiselect>
              </div>
              <div class="form-group col-md-3">
                <label>Filter by Genre</label>
                <button type="buttom" class="btn btn-primary btn-xs pull-right" @click="selected_genres=[]">Clear</button>
                <multiselect v-model="selected_genres" :showLabels="false" :options="available_genres" :multiple="true" :close-on-select="false" :clear-on-select="false" :hide-selected="true" :limit="5"></multiselect>
              </div>
              <div class="form-group col-md-3">
                <label>Filter by Platform</label>
                <button type="buttom" class="btn btn-primary btn-xs pull-right" @click="selected_genres=[]">Clear</button>
                <multiselect v-model="selected_platforms" :showLabels="false" :options="available_platforms" :multiple="true" :close-on-select="false" :clear-on-select="false" :hide-selected="true" :limit="5"></multiselect>
              </div>
              <div class=" form-group col-md-3">
              <label>Sort By Score</label>
              <multiselect v-model="selected_score_sort" :options="available_score_sort" :searchable="false" :close-on-select="false" :clear-on-select="false" :hide-selected="true" :showLabels="false"></multiselect>
              </div>
            </form>
          <paginate-links for="gamelist" class="pagination pagination-sm pull-right" :limit="10"></paginate-links>
        </div>
        <div class="row">
            <paginate name="gamelist" :list="gamelist" :per="12" tag="div">
                <div  class="col-md-4 col-sm-6 col-xs-12" v-for="game in paginated('gamelist')">
                <div  class="panel panel-primary">
                    <div class="panel-heading">
                        <h3 class="panel-title">{{game.title}}<span v-if="game.editors_choice=='Y'" class="badge pull-right">Editor's Pick</span></h3>
                    </div>
                    <div class="panel-body">
                        <br> Platform: {{game.platform}}
                    </div>
                    <div class="panel-footer">
                        Genre: {{game.genre}}<span class="badge pull-right">{{game.score}}</span>
                    </div>
                </div>
                </div>
            </paginate>
            <paginate-links for="gamelist" class="pagination pagination-sm pull-right text-center" :limit="10"></paginate-links>
        </div>
    </div>
</template>
<script>
import auth from '../auth'
import Vue from 'vue'
import axios from 'axios'
import Multiselect from 'vue-multiselect'
import VuePaginate from 'vue-paginate'
Vue.use(VuePaginate)

axios.defaults.headers.common['Authorization'] = auth.getAuthHeaderToSend();
export default {
    components: {Multiselect},
    beforeMount: function() {
        var self = this;
        axios.get(auth.urls.SITE_URL + 'api/v1/gamelist/').then(function(response) {
                if (response.data != null) {
                    self.initial_gamelist = response.data;;;
                      response.data.forEach(function(element) {
                        console.log()
                        if(self.available_genres.indexOf(element.genre)==-1) {
                            self.available_genres.push(element.genre);
                        }
                        if(self.available_platforms.indexOf(element.platform)==-1) {
                            self.available_platforms.push(element.platform);
                        }
                        if(self.available_titles.indexOf(element.title)==-1) {
                            self.available_titles.push(element.title);
                        }
                      });

                }
            })
            .catch(function(err) {
                self.error = err
            });
    },
    data() {
        return {
            initial_gamelist: [],
            paginate: ['gamelist'],
            available_genres: [],
            selected_genres: [],
            available_platforms: [],
            selected_platforms: [],
            available_titles: [],
            title_search: "",
            filtered_titles: [],
            noResult: "Oops! No elements found. Consider changing the search query.",
            available_score_sort: ["None", "Ascending", "Descending"],
            selected_score_sort: ""

        }
    },
    computed:{
        gamelist:function(){
            var self = this;
            var filtered_list = this.initial_gamelist.filter(function(elem){
                var flag = true;
                if(self.title_search!=""){
                    if(elem.title != self.title_search){
                        return false
                    }
                }
                if(self.selected_genres.length > 0){
                    if(self.selected_genres.indexOf(elem.genre) < 0){
                        return false
                    }
                }
                if(self.selected_platforms.length > 0){
                    if(self.selected_platforms.indexOf(elem.platform) < 0){
                        return false
                    }
                }
                return true;

            });
            if(this.selected_score_sort=="Ascending"){
                filtered_list.sort(function(a,b) {return (a.score > b.score) ? 1 : ((b.score > a.score) ? -1 : 0);} );
            }
            if(this.selected_score_sort=="Descending"){
                filtered_list.sort(function(a,b) {return (a.score < b.score) ? 1 : ((b.score < a.score) ? -1 : 0);} );
            }
            
            return filtered_list;
        }
    },
    methods:{
        title_search_change: function(query){
            if(query.length>1){
                this.filtered_titles = this.available_titles.filter(function(elem){
                    return elem.indexOf(query)==-1;
                });
                this.noResult = "Oops! No elements found.";
            }else{
                this.filtered_titles = [];
                this.noResult = "Type 2 or more characters.";
            }

        }
    }

}
</script>
<style scoped>

</style>
