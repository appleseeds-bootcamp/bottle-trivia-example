$(document).ready(function(){
    $("#question-form").submit(function(e){
       e.preventDefault();
       let form = $(this);
       let formIsValid = true;
       form.find("input").each(function(){
          let field = $(this);
          if (!field.val()){
             field.after($("<span>Required</span>"));
             formIsValid = false;
          }
       });
       if (formIsValid){
          $.post("/add_question",form.serialize(),function(res){   
             alert(res);
          });
       }
       return false;
    });
 });
 