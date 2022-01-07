// AJAX FOR Category Delete : 
$('tbody').on('click','.delete-category',function(){
    console.log('delete button clicked');
    let id = $(this).attr('data-sid');
    console.log(id);
    mydata = {pid:id, 'csrfmiddlewaretoken': '{{ csrf_token }}'}
    mythis = this;
    console.log(mythis)
    $.ajax({
        url : "{% url 'deleteCat' %}",
        method : "POST",
        data : mydata,
        success : function(data){
            console.log(data);
            if (data.status==1){
                console.log("Category Deleted Successfully")
                $(mythis).closest("tr").fadeOut();
            }
            if (data.status==0){
                console.log("Unable To Delete Category")
            }
        },
    });
});

// AJAX FOR Product Delete : 
$('tbody').on('click','.delete-product',function(){
    console.log('delete button clicked');
    let id = $(this).attr('data-sid');
    console.log(id);
    mydata = {pid:id, 'csrfmiddlewaretoken': '{{ csrf_token }}'}
    mythis = this;
    console.log(mythis)
    $.ajax({
        url : "{% url 'deleteproduct' %}",
        method : "POST",
        data : mydata,
        success : function(data){
            console.log(data);
            if (data.status==1){
                console.log("Product Deleted Successfully")
                $(mythis).closest("tr").fadeOut();
            }
            if (data.status==0){
                console.log("Unable To Delete Product")
            }
        },
    });
});

// AJAX FOR User Page Delete : 
$('tbody').on('click','.delete-usr',function(){
    console.log('delete button clicked');
    let id = $(this).attr('data-sid');
    console.log(id);
    mydata = {pid:id, 'csrfmiddlewaretoken': '{{ csrf_token }}'}
    mythis = this;
    console.log(mythis)
    $.ajax({
        url : "{% url 'deleteuser' %}",
        method : "POST",
        data : mydata,
        success : function(data){
            console.log(data);
            if (data.status==1){
                console.log("User Deleted Successfully")
                $(mythis).closest("tr").fadeOut();
            }
            if (data.status==0){
                console.log("Unable To Delete User")
            }
        },
    });
});

// AJAX FOR Static Page Delete : 
$('tbody').on('click','.delete-page',function(){
    console.log('delete button clicked');
    let id = $(this).attr('data-sid');
    console.log(id);
    mydata = {pid:id, 'csrfmiddlewaretoken': '{{ csrf_token }}'}
    mythis = this;
    console.log(mythis)
    $.ajax({
        url : "{% url 'deletepage' %}",
        method : "POST",
        data : mydata,
        success : function(data){
            console.log(data);
            if (data.status==1){
                console.log("Page Deleted Successfully")
                $(mythis).closest("tr").fadeOut();
            }
            if (data.status==0){
                console.log("Unable To Delete Page")
            }
        },
    });
});

// AJAX FOR Banner Page Delete : 
$('tbody').on('click','.delete-banner',function(){
    console.log('delete button clicked');
    let id = $(this).attr('data-sid');
    console.log(id);
    mydata = {pid:id, 'csrfmiddlewaretoken': '{{ csrf_token }}'}
    mythis = this;
    console.log(mythis)
    $.ajax({
        url : "{% url 'deletebanner' %}",
        method : "POST",
        data : mydata,
        success : function(data){
            console.log(data);
            if (data.status==1){
                console.log("Banner Deleted Successfully")
                $(mythis).closest("tr").fadeOut();
            }
            if (data.status==0){
                console.log("Unable To Delete Banner")
            }
        },
    });
});

// Show Password Contain :
$('div.password').on('click','i.mdi-eye',function(){
    $('.password-input').attr('type','password').hide();
    $('.password-input').attr('type','text').show();
    $('i.password').removeClass('mdi-eye');
    $('i.password').addClass('mdi-eye-off');  
});

// Hide Password Contain :
$('div.password').on('click','i.mdi-eye-off',function(){
    $('.password-input').attr('type','text').hide();
    $('.password-input').attr('type','password').show();
    $('i.password').removeClass('mdi-eye-off');
    $('i.password').addClass('mdi-eye');
});
