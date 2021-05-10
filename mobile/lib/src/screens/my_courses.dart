import 'package:flutter/material.dart';
import 'package:mobile/src/global_data.dart';
import '../widgets/course_card.dart';
import '../widgets/add_course.dart';
import '../models/course.dart' show Course;
import '../services/course_serv.dart' show getUserCourses;
import '../global_data.dart' show globalSessionData;

class MyCourses extends StatefulWidget {
  MyCourses({Key key}) : super(key: key);

  @override
  _MyCoursesState createState() => _MyCoursesState();
}

class _MyCoursesState extends State<MyCourses> {
  List<Course> userCourses;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: Text("My Courses"),
          actions: [
            IconButton(
              icon: Icon(
                Icons.account_circle,
                size: 35,
              ),
              onPressed: () {
                Navigator.pushNamed(context, '/profile');
              },
            ),
            IconButton(
              icon: Icon(Icons.logout),
              onPressed: () {
                clearSessionData();
                Navigator.popAndPushNamed(context, '/sign-in');
              },
            ),
            SizedBox(width: 20),
          ],
        ),
        body: Container(
          padding: EdgeInsets.symmetric(horizontal: 20.0),
          child: SingleChildScrollView(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                SizedBox(height: 20.0),
                AddCourse(addToCourseList: _addUserCourse),
                SizedBox(height: 10.0),
                buildCourseList(),
              ],
            ),
          ),
        ));
  }

  void _addUserCourse(Course newCourse) {
    print('Course is being added');
    print(newCourse);
    setState(() {
      userCourses.add(newCourse);
    });
  }

  buildCourseList() {
    return FutureBuilder(
      future: getUserCourses(globalSessionData.userId),
      builder: (context, snapshot) {
        if (snapshot.connectionState == ConnectionState.done) {
          // Set state here
          userCourses = snapshot.data;
          print('Gotten Users courses. Time to build');

          return ListView.separated(
            physics: ClampingScrollPhysics(),
            shrinkWrap: true,
            itemCount: userCourses.length,
            itemBuilder: (context, index) => listItem(context, index),
            separatorBuilder: (context, index) => SizedBox(height: 5),
          );
        }
        return Container();
      },
    );
  }

  Widget listItem(BuildContext context, int index) {
    return Container(
      child: CourseCard(userCourses[index].code, userCourses[index].title),
    );
  }
}

List<Map<String, String>> courses = [
  {'code': 'INSY402', 'title': "Internet Technologies"},
  {'code': 'COSC423', 'title': "Artificial Intelligence"},
  {'code': 'COSC417', 'title': "Database Design and Management"},
  {'code': 'COSC430', 'title': "Hands-on Java Training"},
];

List<Map<String, String>> coursesList = [
  {'code': 'INSY402', 'title': "Internet Technologies"},
  {'code': 'COSC423', 'title': "Artificial Intelligence"},
  {'code': 'COSC417', 'title': "Database Design and Management"},
  {'code': 'COSC430', 'title': "Hands-on Java Training"},
  {'code': 'INSY404', 'title': "Introduction to Object Oriented Design"},
  {'code': 'COSC418', 'title': "Introduction to Analog Computing"},
  {'code': 'COSC408', 'title': "Modelling and Simulations"},
];
